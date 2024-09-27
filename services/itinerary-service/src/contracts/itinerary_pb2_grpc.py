# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import itinerary_pb2 as itinerary__pb2


class ItineraryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetItinerary = channel.unary_unary(
                '/itinerary.Itinerary/GetItinerary',
                request_serializer=itinerary__pb2.GetItineraryRequest.SerializeToString,
                response_deserializer=itinerary__pb2.GetItineraryReply.FromString,
                )


class ItineraryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetItinerary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ItineraryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetItinerary': grpc.unary_unary_rpc_method_handler(
                    servicer.GetItinerary,
                    request_deserializer=itinerary__pb2.GetItineraryRequest.FromString,
                    response_serializer=itinerary__pb2.GetItineraryReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'itinerary.Itinerary', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Itinerary(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetItinerary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/itinerary.Itinerary/GetItinerary',
            itinerary__pb2.GetItineraryRequest.SerializeToString,
            itinerary__pb2.GetItineraryReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
