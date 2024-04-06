from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import grpc
from concurrent import futures
import contracts.user_pb2 as user
import contracts.user_pb2_grpc as user_grpc

app = FastAPI()

class User(BaseModel):
    user_id: int
    name: str
    email: str

class UserServicer(user_grpc.UserServicer):
    def __init__(self):
        self.users = {}

    def CreateUser(self, request, context):
        user = User(user_id=request.user_id, name=request.name, email=request.email)
        if user.user_id in self.users:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("User ID already exists")
            return user.Empty()
        self.users[user.user_id] = user
        return user.Empty()

    def GetUser(self, request, context):
        if request.user_id not in self.users:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return user.User()
        user = self.users[request.user_id]
        return user.User(user_id=user.user_id, name=user.name, email=user.email)

    def UpdateUser(self, request, context):
        if request.user_id not in self.users:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return user.Empty()
        user = User(user_id=request.user_id, name=request.name, email=request.email)
        self.users[user.user_id] = user
        return user.Empty()

    def DeleteUser(self, request, context):
        if request.user_id not in self.users:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return user.Empty()
        del self.users[request.user_id]
        return user.Empty()

@app.on_event("startup")
async def startup_event():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

@app.on_event("shutdown")
async def shutdown_event():
    server.stop(0)