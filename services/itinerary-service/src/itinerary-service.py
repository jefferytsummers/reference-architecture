from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI;
import grpc
import contracts.itinerary_pb2 as itinerary_
import contracts.itinerary_pb2_grpc as itinerary_grpc
from grpc_reflection.v1alpha import reflection

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    print('Itinerary Service starting...')
    app.state.server = grpc.aio.server()
    app.state.itinerary_servicer = ItineraryServicer(app)
    itinerary_grpc.add_ItineraryServicer_to_server(app.state.itinerary_servicer, app.state.server)
    SERVICE_NAMES = (
        'itinerary.Itinerary',
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, app.state.server)
    app.state.server.add_insecure_port('127.0.0.1:50052')
    await app.state.server.start()
    yield
    print('Itinerary Service shutting down...')
    await app.state.server.stop(0)
    pass

itinerary_service = FastAPI(lifespan=lifespan)

class ItineraryServicer(itinerary_grpc.ItineraryServicer):
    def __init__(self, app: FastAPI):
        self.app = app

    async def GetItinerary(self, request: itinerary_.GetItineraryRequest, context) -> itinerary_.GetItineraryReply:
        return itinerary_.GetItineraryReply(success=True, message="Itinerary retrieved successfully")