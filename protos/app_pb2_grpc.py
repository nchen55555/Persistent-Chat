# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protos import app_pb2 as protos_dot_app__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protos/app_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AppStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RPCLogin = channel.unary_unary(
                '/App/RPCLogin',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCCreateAccount = channel.unary_unary(
                '/App/RPCCreateAccount',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCListAccount = channel.unary_unary(
                '/App/RPCListAccount',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCSendMessage = channel.unary_unary(
                '/App/RPCSendMessage',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCReadMessage = channel.unary_unary(
                '/App/RPCReadMessage',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCDeleteMessage = channel.unary_unary(
                '/App/RPCDeleteMessage',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCDeleteAccount = channel.unary_unary(
                '/App/RPCDeleteAccount',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCGetInstantMessages = channel.unary_unary(
                '/App/RPCGetInstantMessages',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCLogout = channel.unary_unary(
                '/App/RPCLogout',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCHeartbeat = channel.unary_unary(
                '/App/RPCHeartbeat',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCUpdateLeader = channel.unary_unary(
                '/App/RPCUpdateLeader',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCGetLeaderInfo = channel.unary_unary(
                '/App/RPCGetLeaderInfo',
                request_serializer=protos_dot_app__pb2.Request.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)
        self.RPCSyncData = channel.unary_unary(
                '/App/RPCSyncData',
                request_serializer=protos_dot_app__pb2.SyncDataRequest.SerializeToString,
                response_deserializer=protos_dot_app__pb2.Response.FromString,
                _registered_method=True)


class AppServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RPCLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCCreateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCListAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCSendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCReadMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCDeleteMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCDeleteAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCGetInstantMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCLogout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCHeartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCUpdateLeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCGetLeaderInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RPCSyncData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RPCLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCLogin,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCCreateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCCreateAccount,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCListAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCListAccount,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCSendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCSendMessage,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCReadMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCReadMessage,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCDeleteMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCDeleteMessage,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCDeleteAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCDeleteAccount,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCGetInstantMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCGetInstantMessages,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCLogout': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCLogout,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCHeartbeat,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCUpdateLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCUpdateLeader,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCGetLeaderInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCGetLeaderInfo,
                    request_deserializer=protos_dot_app__pb2.Request.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
            'RPCSyncData': grpc.unary_unary_rpc_method_handler(
                    servicer.RPCSyncData,
                    request_deserializer=protos_dot_app__pb2.SyncDataRequest.FromString,
                    response_serializer=protos_dot_app__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'App', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('App', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class App(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RPCLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCLogin',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCCreateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCCreateAccount',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCListAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCListAccount',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCSendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCSendMessage',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCReadMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCReadMessage',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCDeleteMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCDeleteMessage',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCDeleteAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCDeleteAccount',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCGetInstantMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCGetInstantMessages',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCLogout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCLogout',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCHeartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCHeartbeat',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCUpdateLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCUpdateLeader',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCGetLeaderInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCGetLeaderInfo',
            protos_dot_app__pb2.Request.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RPCSyncData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/App/RPCSyncData',
            protos_dot_app__pb2.SyncDataRequest.SerializeToString,
            protos_dot_app__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
