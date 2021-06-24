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
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.debugger_v2.types import data
from google.cloud.debugger_v2.types import debugger
from .transports.base import Debugger2Transport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import Debugger2GrpcAsyncIOTransport
from .client import Debugger2Client


class Debugger2AsyncClient:
    """The Debugger service provides the API that allows users to
    collect run-time information from a running application, without
    stopping or slowing it down and without modifying its state.  An
    application may include one or more replicated processes
    performing the same work.
    A debugged application is represented using the Debuggee
    concept. The Debugger service provides a way to query for
    available debuggees, but does not provide a way to create one.
    A debuggee is created using the Controller service, usually by
    running a debugger agent with the application.
    The Debugger service enables the client to set one or more
    Breakpoints on a Debuggee and collect the results of the set
    Breakpoints.
    """

    _client: Debugger2Client

    DEFAULT_ENDPOINT = Debugger2Client.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = Debugger2Client.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        Debugger2Client.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        Debugger2Client.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(Debugger2Client.common_folder_path)
    parse_common_folder_path = staticmethod(Debugger2Client.parse_common_folder_path)
    common_organization_path = staticmethod(Debugger2Client.common_organization_path)
    parse_common_organization_path = staticmethod(
        Debugger2Client.parse_common_organization_path
    )
    common_project_path = staticmethod(Debugger2Client.common_project_path)
    parse_common_project_path = staticmethod(Debugger2Client.parse_common_project_path)
    common_location_path = staticmethod(Debugger2Client.common_location_path)
    parse_common_location_path = staticmethod(
        Debugger2Client.parse_common_location_path
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
            Debugger2AsyncClient: The constructed client.
        """
        return Debugger2Client.from_service_account_info.__func__(Debugger2AsyncClient, info, *args, **kwargs)  # type: ignore

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
            Debugger2AsyncClient: The constructed client.
        """
        return Debugger2Client.from_service_account_file.__func__(Debugger2AsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> Debugger2Transport:
        """Returns the transport used by the client instance.

        Returns:
            Debugger2Transport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(Debugger2Client).get_transport_class, type(Debugger2Client)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, Debugger2Transport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the debugger2 client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.Debugger2Transport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
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

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = Debugger2Client(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def set_breakpoint(
        self,
        request: debugger.SetBreakpointRequest = None,
        *,
        debuggee_id: str = None,
        breakpoint_: data.Breakpoint = None,
        client_version: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> debugger.SetBreakpointResponse:
        r"""Sets the breakpoint to the debuggee.

        Args:
            request (:class:`google.cloud.debugger_v2.types.SetBreakpointRequest`):
                The request object. Request to set a breakpoint
            debuggee_id (:class:`str`):
                Required. ID of the debuggee where
                the breakpoint is to be set.

                This corresponds to the ``debuggee_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            breakpoint_ (:class:`google.cloud.debugger_v2.types.Breakpoint`):
                Required. Breakpoint specification to set. The field
                ``location`` of the breakpoint must be set.

                This corresponds to the ``breakpoint_`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            client_version (:class:`str`):
                Required. The client version making the call. Schema:
                ``domain/type/version`` (e.g.,
                ``google.com/intellij/v1``).

                This corresponds to the ``client_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.SetBreakpointResponse:
                Response for setting a breakpoint.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee_id, breakpoint_, client_version])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = debugger.SetBreakpointRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if debuggee_id is not None:
            request.debuggee_id = debuggee_id
        if breakpoint_ is not None:
            request.breakpoint_ = breakpoint_
        if client_version is not None:
            request.client_version = client_version

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_breakpoint,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_breakpoint(
        self,
        request: debugger.GetBreakpointRequest = None,
        *,
        debuggee_id: str = None,
        breakpoint_id: str = None,
        client_version: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> debugger.GetBreakpointResponse:
        r"""Gets breakpoint information.

        Args:
            request (:class:`google.cloud.debugger_v2.types.GetBreakpointRequest`):
                The request object. Request to get breakpoint
                information.
            debuggee_id (:class:`str`):
                Required. ID of the debuggee whose
                breakpoint to get.

                This corresponds to the ``debuggee_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            breakpoint_id (:class:`str`):
                Required. ID of the breakpoint to
                get.

                This corresponds to the ``breakpoint_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            client_version (:class:`str`):
                Required. The client version making the call. Schema:
                ``domain/type/version`` (e.g.,
                ``google.com/intellij/v1``).

                This corresponds to the ``client_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.GetBreakpointResponse:
                Response for getting breakpoint
                information.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee_id, breakpoint_id, client_version])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = debugger.GetBreakpointRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if debuggee_id is not None:
            request.debuggee_id = debuggee_id
        if breakpoint_id is not None:
            request.breakpoint_id = breakpoint_id
        if client_version is not None:
            request.client_version = client_version

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_breakpoint,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def delete_breakpoint(
        self,
        request: debugger.DeleteBreakpointRequest = None,
        *,
        debuggee_id: str = None,
        breakpoint_id: str = None,
        client_version: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the breakpoint from the debuggee.

        Args:
            request (:class:`google.cloud.debugger_v2.types.DeleteBreakpointRequest`):
                The request object. Request to delete a breakpoint.
            debuggee_id (:class:`str`):
                Required. ID of the debuggee whose
                breakpoint to delete.

                This corresponds to the ``debuggee_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            breakpoint_id (:class:`str`):
                Required. ID of the breakpoint to
                delete.

                This corresponds to the ``breakpoint_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            client_version (:class:`str`):
                Required. The client version making the call. Schema:
                ``domain/type/version`` (e.g.,
                ``google.com/intellij/v1``).

                This corresponds to the ``client_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee_id, breakpoint_id, client_version])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = debugger.DeleteBreakpointRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if debuggee_id is not None:
            request.debuggee_id = debuggee_id
        if breakpoint_id is not None:
            request.breakpoint_id = breakpoint_id
        if client_version is not None:
            request.client_version = client_version

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_breakpoint,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    async def list_breakpoints(
        self,
        request: debugger.ListBreakpointsRequest = None,
        *,
        debuggee_id: str = None,
        client_version: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> debugger.ListBreakpointsResponse:
        r"""Lists all breakpoints for the debuggee.

        Args:
            request (:class:`google.cloud.debugger_v2.types.ListBreakpointsRequest`):
                The request object. Request to list breakpoints.
            debuggee_id (:class:`str`):
                Required. ID of the debuggee whose
                breakpoints to list.

                This corresponds to the ``debuggee_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            client_version (:class:`str`):
                Required. The client version making the call. Schema:
                ``domain/type/version`` (e.g.,
                ``google.com/intellij/v1``).

                This corresponds to the ``client_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.ListBreakpointsResponse:
                Response for listing breakpoints.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee_id, client_version])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = debugger.ListBreakpointsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if debuggee_id is not None:
            request.debuggee_id = debuggee_id
        if client_version is not None:
            request.client_version = client_version

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_breakpoints,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_debuggees(
        self,
        request: debugger.ListDebuggeesRequest = None,
        *,
        project: str = None,
        client_version: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> debugger.ListDebuggeesResponse:
        r"""Lists all the debuggees that the user has access to.

        Args:
            request (:class:`google.cloud.debugger_v2.types.ListDebuggeesRequest`):
                The request object. Request to list debuggees.
            project (:class:`str`):
                Required. Project number of a Google
                Cloud project whose debuggees to list.

                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            client_version (:class:`str`):
                Required. The client version making the call. Schema:
                ``domain/type/version`` (e.g.,
                ``google.com/intellij/v1``).

                This corresponds to the ``client_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.ListDebuggeesResponse:
                Response for listing debuggees.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, client_version])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = debugger.ListDebuggeesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project is not None:
            request.project = project
        if client_version is not None:
            request.client_version = client_version

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_debuggees,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

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


__all__ = ("Debugger2AsyncClient",)
