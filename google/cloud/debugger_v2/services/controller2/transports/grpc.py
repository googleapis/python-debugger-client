# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, grpc_helpers
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
import grpc  # type: ignore

from google.cloud.debugger_v2.types import controller

from .base import DEFAULT_CLIENT_INFO, Controller2Transport


class Controller2GrpcTransport(Controller2Transport):
    """gRPC backend transport for Controller2.

    The Controller service provides the API for orchestrating a
    collection of debugger agents to perform debugging tasks. These
    agents are each attached to a process of an application which may
    include one or more replicas.

    The debugger agents register with the Controller to identify the
    application being debugged, the Debuggee. All agents that register
    with the same data, represent the same Debuggee, and are assigned
    the same ``debuggee_id``.

    The debugger agents call the Controller to retrieve the list of
    active Breakpoints. Agents with the same ``debuggee_id`` get the
    same breakpoints list. An agent that can fulfill the breakpoint
    request updates the Controller with the breakpoint result. The
    controller selects the first result received and discards the rest
    of the results. Agents that poll again for active breakpoints will
    no longer have the completed breakpoint in the list and should
    remove that breakpoint from their attached process.

    The Controller service does not provide a way to retrieve the
    results of a completed breakpoint. This functionality is available
    using the Debugger service.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "clouddebugger.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[grpc.Channel] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "clouddebugger.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        return self._grpc_channel

    @property
    def register_debuggee(
        self,
    ) -> Callable[
        [controller.RegisterDebuggeeRequest], controller.RegisterDebuggeeResponse
    ]:
        r"""Return a callable for the register debuggee method over gRPC.

        Registers the debuggee with the controller service.

        All agents attached to the same application must call this
        method with exactly the same request content to get back the
        same stable ``debuggee_id``. Agents should call this method
        again whenever ``google.rpc.Code.NOT_FOUND`` is returned from
        any controller method.

        This protocol allows the controller service to disable
        debuggees, recover from data loss, or change the ``debuggee_id``
        format. Agents must handle ``debuggee_id`` value changing upon
        re-registration.

        Returns:
            Callable[[~.RegisterDebuggeeRequest],
                    ~.RegisterDebuggeeResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "register_debuggee" not in self._stubs:
            self._stubs["register_debuggee"] = self.grpc_channel.unary_unary(
                "/google.devtools.clouddebugger.v2.Controller2/RegisterDebuggee",
                request_serializer=controller.RegisterDebuggeeRequest.serialize,
                response_deserializer=controller.RegisterDebuggeeResponse.deserialize,
            )
        return self._stubs["register_debuggee"]

    @property
    def list_active_breakpoints(
        self,
    ) -> Callable[
        [controller.ListActiveBreakpointsRequest],
        controller.ListActiveBreakpointsResponse,
    ]:
        r"""Return a callable for the list active breakpoints method over gRPC.

        Returns the list of all active breakpoints for the debuggee.

        The breakpoint specification (``location``, ``condition``, and
        ``expressions`` fields) is semantically immutable, although the
        field values may change. For example, an agent may update the
        location line number to reflect the actual line where the
        breakpoint was set, but this doesn't change the breakpoint
        semantics.

        This means that an agent does not need to check if a breakpoint
        has changed when it encounters the same breakpoint on a
        successive call. Moreover, an agent should remember the
        breakpoints that are completed until the controller removes them
        from the active list to avoid setting those breakpoints again.

        Returns:
            Callable[[~.ListActiveBreakpointsRequest],
                    ~.ListActiveBreakpointsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_active_breakpoints" not in self._stubs:
            self._stubs["list_active_breakpoints"] = self.grpc_channel.unary_unary(
                "/google.devtools.clouddebugger.v2.Controller2/ListActiveBreakpoints",
                request_serializer=controller.ListActiveBreakpointsRequest.serialize,
                response_deserializer=controller.ListActiveBreakpointsResponse.deserialize,
            )
        return self._stubs["list_active_breakpoints"]

    @property
    def update_active_breakpoint(
        self,
    ) -> Callable[
        [controller.UpdateActiveBreakpointRequest],
        controller.UpdateActiveBreakpointResponse,
    ]:
        r"""Return a callable for the update active breakpoint method over gRPC.

        Updates the breakpoint state or mutable fields. The entire
        Breakpoint message must be sent back to the controller service.

        Updates to active breakpoint fields are only allowed if the new
        value does not change the breakpoint specification. Updates to
        the ``location``, ``condition`` and ``expressions`` fields
        should not alter the breakpoint semantics. These may only make
        changes such as canonicalizing a value or snapping the location
        to the correct line of code.

        Returns:
            Callable[[~.UpdateActiveBreakpointRequest],
                    ~.UpdateActiveBreakpointResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_active_breakpoint" not in self._stubs:
            self._stubs["update_active_breakpoint"] = self.grpc_channel.unary_unary(
                "/google.devtools.clouddebugger.v2.Controller2/UpdateActiveBreakpoint",
                request_serializer=controller.UpdateActiveBreakpointRequest.serialize,
                response_deserializer=controller.UpdateActiveBreakpointResponse.deserialize,
            )
        return self._stubs["update_active_breakpoint"]

    def close(self):
        self.grpc_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("Controller2GrpcTransport",)
