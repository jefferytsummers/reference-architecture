from contextlib import asynccontextmanager
from typing import AsyncGenerator, List, Dict
import grpc
from fastapi import FastAPI
import contracts.command_pb2 as command_
import contracts.command_pb2_grpc as command_grpc

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    print('Command Queue starting up...')
    print('ADDING SERVICERS')
    app.state.server = grpc.aio.server()
    command_grpc.add_CommandQueueServiceServicer_to_server(CommandQueueServiceServicer(), app.state.server)
    print('\033[1;32m  CommandQueueServiceServicer added to grpc server...')
    app.state.server.add_insecure_port('[::]:50051')
    print('SERVICERS ADDED')
    await app.state.server.start()
    print('Command Queue successfully spun up. Contracts sent over :50051')
    yield
    print('Command queue shutting down...')
    await app.state.server.stop(0)
    print("Command Queue Successfully spun down.")

app = FastAPI(lifespan=lifespan)

class CommandQueueServiceServicer(command_grpc.CommandQueueServiceServicer):
    def __init__(self):
        self.command_queue: Dict[str, List[command_.Command]] = {}

    async def EnqueueCommand(self, request: command_.EnqueueCommandRequest, context: grpc.aio.ServicerContext) -> command_.EnqueueCommandResponse:
        command: command_.Command = request.command
        service_name: str = command.service_name
        if service_name not in self.command_queue:
            self.command_queue[service_name] = []
        self.command_queue[service_name].append(command)
        return command_.EnqueueCommandResponse(success=True, message="Command enqueued successfully")

    async def DequeueCommand(self, request: command_.DequeueCommandRequest, context: grpc.aio.ServicerContext) -> command_.DequeueCommandResponse:
        service_name: str = request.service_name
        command_id: str = request.command_id
        if service_name in self.command_queue:
            for command in self.command_queue[service_name]:
                if command.command_id == command_id:
                    self.command_queue[service_name].remove(command)
                    return command_.DequeueCommandResponse(command=command, success=True, message="Command dequeued successfully")
        return command_.DequeueCommandResponse(success=False, message="Command not found")

    async def RetryCommand(self, request: command_.RetryCommandRequest, context: grpc.aio.ServicerContext) -> command_.RetryCommandResponse:
        command_id: str = request.command_id
        service_name: str = request.service_name
        for commands in self.command_queue.values():
            for command in commands:
                if command.command_id == command_id and command.service_name == service_name:
                    command.retry_count += 1
                    return command_.RetryCommandResponse(success=True, message="Command retry count incremented")
        return command_.RetryCommandResponse(success=False, message="Command not found")

    async def logQueueState(self, context: grpc.aio.ServicerContext) -> command_.LogQueueStateResponse:
        pass