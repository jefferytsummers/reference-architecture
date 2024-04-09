from contextlib import asynccontextmanager
from fastapi import FastAPI;
import grpc
import contracts.itinerary_pb2 as itinerary_
import contracts.itinerary_pb2_grpc as itinerary_grpc

@asynccontextmanager
def lifespan(app: FastAPI):
    print('Itinerary Service starting...')
    app.state.server = grpc.aio.server()
    app.state.command_queue_servicer = ItineraryServicer(app)
    itinerary_grpc.add_ItineraryServicer_to_server(app.state.command_queue_servicer, app.state.server)
    yield
    print('Itinerary Service shutting down...')
    pass

app = FastAPI(lifespan=lifespan)

class ItineraryServicer(itinerary_grpc.ItineraryServicer):
    def __init__(self, app: FastAPI):
        self.app = app

    async def GetItinerary(self, request, context):
        return super().GetItinerary(request, context)