import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator, List, Dict
import grpc
from fastapi import FastAPI
import contracts.command_pb2 as command_
import contracts.command_pb2_grpc as command_grpc
from google.protobuf.wrappers_pb2 import BoolValue

async def process_command_queue(app: FastAPI):
    while True:
        for service_name, queue in app.state.command_queue_servicer.command_queue.items():
            if not queue.empty():
                command = await queue.get()
                # Process the command here
                print(f"Processing command for service: {service_name}")
                print(f"Command ID: {command.command_id}")
                print(f"Command Type: {command.command_type}")
                print(f"Payload: {command.payload}")
                # Add your command processing logic here
                print(f"Command processed successfully for service: {service_name}")
            else:
                print(f"No commands in the queue for service: {service_name}")

        print("All queues checked. Waiting for new commands...")
        await asyncio.sleep(5)  # Adjust the sleep duration as needed

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    print('Command Queue starting up...')
    print('ADDING SERVICERS')
    app.state.server = grpc.aio.server()
    app.state.command_queue_servicer = CommandQueueServicer(app)
    command_grpc.add_CommandQueueServiceServicer_to_server(app.state.command_queue_servicer, app.state.server)
    app.state.command_queue_task = asyncio.create_task(process_command_queue(app))
    print('\033[1;32m CommandQueueServiceServicer added to grpc server...')
    app.state.server.add_insecure_port('[::]:50051')
    print('SERVICERS ADDED')
    await app.state.server.start()
    print('Command Queue successfully spun up. Contracts sent over :50051')
    yield
    print('Command queue shutting down...')
    app.state.command_queue_task.cancel()
    await app.state.command_queue_task
    await app.state.server.stop(0)
    print("Command Queue Successfully spun down.")

app = FastAPI(lifespan=lifespan)

app = FastAPI(lifespan=lifespan)

class CommandQueueServicer(command_grpc.CommandQueueServiceServicer):
    def __init__(self, app: FastAPI):
        self.command_queue: Dict[str, asyncio.Queue[command_.Command]] = {}
        self.app = app

    async def EnqueueCommand(self, request: command_.EnqueueCommandRequest, context: grpc.aio.ServicerContext) -> command_.EnqueueCommandResponse:
        command: command_.Command = request.command
        service_name: str = command.service_name

        if service_name not in self.command_queue:
            self.command_queue[service_name] = asyncio.Queue()

        await self.command_queue[service_name].put(command)
        return command_.EnqueueCommandResponse(success=True, message="Command enqueued successfully")

    async def DequeueCommand(self, request: command_.DequeueCommandRequest, context: grpc.aio.ServicerContext) -> command_.DequeueCommandResponse:
        service_name: str = request.service_name
        command_id: str = request.command_id

        if service_name in self.command_queue:
            queue = self.command_queue[service_name]
            command = await queue.get()
            if command.command_id == command_id:
                return command_.DequeueCommandResponse(command=command, success=True, message="Command dequeued successfully")
            else:
                await queue.put(command)

        return command_.DequeueCommandResponse(success=False, message="Command not found")

    async def RetryCommand(self, request: command_.RetryCommandRequest, context: grpc.aio.ServicerContext) -> command_.RetryCommandResponse:
        command_id: str = request.command_id
        service_name: str = request.service_name

        if service_name in self.command_queue:
            queue = self.command_queue[service_name]
            command = await queue.get()
            if command.command_id == command_id:
                command.retry_count += 1
                await queue.put(command)
                return command_.RetryCommandResponse(success=True, message="Command retry count incremented")
            else:
                await queue.put(command)

        return command_.RetryCommandResponse(success=False, message="Command not found")

    async def LogQueueStateCommand(self, request: command_.LogQueueStateCommandRequest, context: grpc.aio.ServicerContext) -> command_.LogQueueStateCommandResponse:
        service_name = request.service_name
        queue_state = []

        if service_name in self.command_queue:
            queue = self.command_queue[service_name]
            commands = list(queue._queue)
            for command in commands:
                queue_state.append(command_.QueueStateByService(
                    command_id=command.command_id,
                    service_name=service_name,
                    processing=False
                ))

        return command_.LogQueueStateCommandResponse(queueState=queue_state)
