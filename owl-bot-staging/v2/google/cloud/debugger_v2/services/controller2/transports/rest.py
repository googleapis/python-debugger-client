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

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.debugger_v2.types import controller

from .base import Controller2Transport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class Controller2RestInterceptor:
    """Interceptor for Controller2.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the Controller2RestTransport.

    .. code-block:: python
        class MyCustomController2Interceptor(Controller2RestInterceptor):
            def pre_list_active_breakpoints(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_active_breakpoints(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_register_debuggee(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_register_debuggee(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_active_breakpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_active_breakpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = Controller2RestTransport(interceptor=MyCustomController2Interceptor())
        client = Controller2Client(transport=transport)


    """
    def pre_list_active_breakpoints(self, request: controller.ListActiveBreakpointsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[controller.ListActiveBreakpointsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_active_breakpoints

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Controller2 server.
        """
        return request, metadata

    def post_list_active_breakpoints(self, response: controller.ListActiveBreakpointsResponse) -> controller.ListActiveBreakpointsResponse:
        """Post-rpc interceptor for list_active_breakpoints

        Override in a subclass to manipulate the response
        after it is returned by the Controller2 server but before
        it is returned to user code.
        """
        return response
    def pre_register_debuggee(self, request: controller.RegisterDebuggeeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[controller.RegisterDebuggeeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for register_debuggee

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Controller2 server.
        """
        return request, metadata

    def post_register_debuggee(self, response: controller.RegisterDebuggeeResponse) -> controller.RegisterDebuggeeResponse:
        """Post-rpc interceptor for register_debuggee

        Override in a subclass to manipulate the response
        after it is returned by the Controller2 server but before
        it is returned to user code.
        """
        return response
    def pre_update_active_breakpoint(self, request: controller.UpdateActiveBreakpointRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[controller.UpdateActiveBreakpointRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_active_breakpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Controller2 server.
        """
        return request, metadata

    def post_update_active_breakpoint(self, response: controller.UpdateActiveBreakpointResponse) -> controller.UpdateActiveBreakpointResponse:
        """Post-rpc interceptor for update_active_breakpoint

        Override in a subclass to manipulate the response
        after it is returned by the Controller2 server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class Controller2RestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: Controller2RestInterceptor


class Controller2RestTransport(Controller2Transport):
    """REST backend transport for Controller2.

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

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(self, *,
            host: str = 'clouddebugger.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[Controller2RestInterceptor] = None,
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

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or Controller2RestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _ListActiveBreakpoints(Controller2RestStub):
        def __hash__(self):
            return hash("ListActiveBreakpoints")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: controller.ListActiveBreakpointsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> controller.ListActiveBreakpointsResponse:
            r"""Call the list active breakpoints method over HTTP.

            Args:
                request (~.controller.ListActiveBreakpointsRequest):
                    The request object. Request to list active breakpoints.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.controller.ListActiveBreakpointsResponse:
                    Response for listing active
                breakpoints.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/controller/debuggees/{debuggee_id}/breakpoints',
            },
            ]
            request, metadata = self._interceptor.pre_list_active_breakpoints(request, metadata)
            pb_request = controller.ListActiveBreakpointsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = controller.ListActiveBreakpointsResponse()
            pb_resp = controller.ListActiveBreakpointsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_active_breakpoints(resp)
            return resp

    class _RegisterDebuggee(Controller2RestStub):
        def __hash__(self):
            return hash("RegisterDebuggee")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: controller.RegisterDebuggeeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> controller.RegisterDebuggeeResponse:
            r"""Call the register debuggee method over HTTP.

            Args:
                request (~.controller.RegisterDebuggeeRequest):
                    The request object. Request to register a debuggee.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.controller.RegisterDebuggeeResponse:
                    Response for registering a debuggee.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/controller/debuggees/register',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_register_debuggee(request, metadata)
            pb_request = controller.RegisterDebuggeeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = controller.RegisterDebuggeeResponse()
            pb_resp = controller.RegisterDebuggeeResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_register_debuggee(resp)
            return resp

    class _UpdateActiveBreakpoint(Controller2RestStub):
        def __hash__(self):
            return hash("UpdateActiveBreakpoint")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: controller.UpdateActiveBreakpointRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> controller.UpdateActiveBreakpointResponse:
            r"""Call the update active breakpoint method over HTTP.

            Args:
                request (~.controller.UpdateActiveBreakpointRequest):
                    The request object. Request to update an active
                breakpoint.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.controller.UpdateActiveBreakpointResponse:
                    Response for updating an active
                breakpoint. The message is defined to
                allow future extensions.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'put',
                'uri': '/v2/controller/debuggees/{debuggee_id}/breakpoints/{breakpoint_.id}',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_update_active_breakpoint(request, metadata)
            pb_request = controller.UpdateActiveBreakpointRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = controller.UpdateActiveBreakpointResponse()
            pb_resp = controller.UpdateActiveBreakpointResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_active_breakpoint(resp)
            return resp

    @property
    def list_active_breakpoints(self) -> Callable[
            [controller.ListActiveBreakpointsRequest],
            controller.ListActiveBreakpointsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListActiveBreakpoints(self._session, self._host, self._interceptor) # type: ignore

    @property
    def register_debuggee(self) -> Callable[
            [controller.RegisterDebuggeeRequest],
            controller.RegisterDebuggeeResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RegisterDebuggee(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_active_breakpoint(self) -> Callable[
            [controller.UpdateActiveBreakpointRequest],
            controller.UpdateActiveBreakpointResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateActiveBreakpoint(self._session, self._host, self._interceptor) # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'Controller2RestTransport',
)
