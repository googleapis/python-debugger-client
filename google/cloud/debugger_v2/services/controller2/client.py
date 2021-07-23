# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
from collections import OrderedDict
from distutils import util
import os
import re
from typing import Callable, Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.debugger_v2.types import controller
from google.cloud.debugger_v2.types import data
from .transports.base import Controller2Transport, DEFAULT_CLIENT_INFO
from .transports.grpc import Controller2GrpcTransport
from .transports.grpc_asyncio import Controller2GrpcAsyncIOTransport


class Controller2ClientMeta(type):
    """Metaclass for the Controller2 client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[Controller2Transport]]
    _transport_registry["grpc"] = Controller2GrpcTransport
    _transport_registry["grpc_asyncio"] = Controller2GrpcAsyncIOTransport

    def get_transport_class(cls, label: str = None,) -> Type[Controller2Transport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class Controller2Client(metaclass=Controller2ClientMeta):
    """The Controller service provides the API for orchestrating a
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
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "clouddebugger.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            Controller2Client: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            Controller2Client: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> Controller2Transport:
        """Returns the transport used by the client instance.

        Returns:
            Controller2Transport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def common_billing_account_path(billing_account: str,) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str,) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder,)

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str,) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization,)

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str,) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(project=project,)

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str,) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project, location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, Controller2Transport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the controller2 client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, Controller2Transport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        # Create SSL credentials for mutual TLS if needed.
        use_client_cert = bool(
            util.strtobool(os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"))
        )

        client_cert_source_func = None
        is_mtls = False
        if use_client_cert:
            if client_options.client_cert_source:
                is_mtls = True
                client_cert_source_func = client_options.client_cert_source
            else:
                is_mtls = mtls.has_default_client_cert_source()
                if is_mtls:
                    client_cert_source_func = mtls.default_client_cert_source()
                else:
                    client_cert_source_func = None

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        else:
            use_mtls_env = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
            if use_mtls_env == "never":
                api_endpoint = self.DEFAULT_ENDPOINT
            elif use_mtls_env == "always":
                api_endpoint = self.DEFAULT_MTLS_ENDPOINT
            elif use_mtls_env == "auto":
                if is_mtls:
                    api_endpoint = self.DEFAULT_MTLS_ENDPOINT
                else:
                    api_endpoint = self.DEFAULT_ENDPOINT
            else:
                raise MutualTLSChannelError(
                    "Unsupported GOOGLE_API_USE_MTLS_ENDPOINT value. Accepted "
                    "values: never, auto, always"
                )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, Controller2Transport):
            # transport is a Controller2Transport instance.
            if credentials or client_options.credentials_file:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=(
                    Transport == type(self).get_transport_class("grpc")
                    or Transport == type(self).get_transport_class("grpc_asyncio")
                ),
            )

    def register_debuggee(
        self,
        request: controller.RegisterDebuggeeRequest = None,
        *,
        debuggee: data.Debuggee = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> controller.RegisterDebuggeeResponse:
        r"""Registers the debuggee with the controller service.

        All agents attached to the same application must call this
        method with exactly the same request content to get back the
        same stable ``debuggee_id``. Agents should call this method
        again whenever ``google.rpc.Code.NOT_FOUND`` is returned from
        any controller method.

        This protocol allows the controller service to disable
        debuggees, recover from data loss, or change the ``debuggee_id``
        format. Agents must handle ``debuggee_id`` value changing upon
        re-registration.

        Args:
            request (google.cloud.debugger_v2.types.RegisterDebuggeeRequest):
                The request object. Request to register a debuggee.
            debuggee (google.cloud.debugger_v2.types.Debuggee):
                Required. Debuggee information to register. The fields
                ``project``, ``uniquifier``, ``description`` and
                ``agent_version`` of the debuggee must be set.

                This corresponds to the ``debuggee`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.RegisterDebuggeeResponse:
                Response for registering a debuggee.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a controller.RegisterDebuggeeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, controller.RegisterDebuggeeRequest):
            request = controller.RegisterDebuggeeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if debuggee is not None:
                request.debuggee = debuggee

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.register_debuggee]

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_active_breakpoints(
        self,
        request: controller.ListActiveBreakpointsRequest = None,
        *,
        debuggee_id: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> controller.ListActiveBreakpointsResponse:
        r"""Returns the list of all active breakpoints for the debuggee.

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

        Args:
            request (google.cloud.debugger_v2.types.ListActiveBreakpointsRequest):
                The request object. Request to list active breakpoints.
            debuggee_id (str):
                Required. Identifies the debuggee.
                This corresponds to the ``debuggee_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.ListActiveBreakpointsResponse:
                Response for listing active
                breakpoints.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a controller.ListActiveBreakpointsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, controller.ListActiveBreakpointsRequest):
            request = controller.ListActiveBreakpointsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if debuggee_id is not None:
                request.debuggee_id = debuggee_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_active_breakpoints]

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_active_breakpoint(
        self,
        request: controller.UpdateActiveBreakpointRequest = None,
        *,
        debuggee_id: str = None,
        breakpoint_: data.Breakpoint = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> controller.UpdateActiveBreakpointResponse:
        r"""Updates the breakpoint state or mutable fields. The entire
        Breakpoint message must be sent back to the controller service.

        Updates to active breakpoint fields are only allowed if the new
        value does not change the breakpoint specification. Updates to
        the ``location``, ``condition`` and ``expressions`` fields
        should not alter the breakpoint semantics. These may only make
        changes such as canonicalizing a value or snapping the location
        to the correct line of code.

        Args:
            request (google.cloud.debugger_v2.types.UpdateActiveBreakpointRequest):
                The request object. Request to update an active
                breakpoint.
            debuggee_id (str):
                Required. Identifies the debuggee
                being debugged.

                This corresponds to the ``debuggee_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            breakpoint_ (google.cloud.debugger_v2.types.Breakpoint):
                Required. Updated breakpoint information. The field
                ``id`` must be set. The agent must echo all Breakpoint
                specification fields in the update.

                This corresponds to the ``breakpoint_`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.UpdateActiveBreakpointResponse:
                Response for updating an active
                breakpoint. The message is defined to
                allow future extensions.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee_id, breakpoint_])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a controller.UpdateActiveBreakpointRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, controller.UpdateActiveBreakpointRequest):
            request = controller.UpdateActiveBreakpointRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if debuggee_id is not None:
                request.debuggee_id = debuggee_id
            if breakpoint_ is not None:
                request.breakpoint_ = breakpoint_

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_active_breakpoint]

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-debugger-client",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("Controller2Client",)
