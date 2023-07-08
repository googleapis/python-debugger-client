# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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

import dataclasses
import json  # type: ignore
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, path_template, rest_helpers, rest_streaming
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
import grpc  # type: ignore
from requests import __version__ as requests_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.protobuf import empty_pb2  # type: ignore

from google.cloud.debugger_v2.types import debugger

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .base import Debugger2Transport

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class Debugger2RestInterceptor:
    """Interceptor for Debugger2.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the Debugger2RestTransport.

    .. code-block:: python
        class MyCustomDebugger2Interceptor(Debugger2RestInterceptor):
            def pre_delete_breakpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_breakpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_breakpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_breakpoints(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_breakpoints(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_debuggees(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_debuggees(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_breakpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_breakpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = Debugger2RestTransport(interceptor=MyCustomDebugger2Interceptor())
        client = Debugger2Client(transport=transport)


    """

    def pre_delete_breakpoint(
        self,
        request: debugger.DeleteBreakpointRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[debugger.DeleteBreakpointRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_breakpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Debugger2 server.
        """
        return request, metadata

    def pre_get_breakpoint(
        self,
        request: debugger.GetBreakpointRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[debugger.GetBreakpointRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_breakpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Debugger2 server.
        """
        return request, metadata

    def post_get_breakpoint(
        self, response: debugger.GetBreakpointResponse
    ) -> debugger.GetBreakpointResponse:
        """Post-rpc interceptor for get_breakpoint

        Override in a subclass to manipulate the response
        after it is returned by the Debugger2 server but before
        it is returned to user code.
        """
        return response

    def pre_list_breakpoints(
        self,
        request: debugger.ListBreakpointsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[debugger.ListBreakpointsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_breakpoints

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Debugger2 server.
        """
        return request, metadata

    def post_list_breakpoints(
        self, response: debugger.ListBreakpointsResponse
    ) -> debugger.ListBreakpointsResponse:
        """Post-rpc interceptor for list_breakpoints

        Override in a subclass to manipulate the response
        after it is returned by the Debugger2 server but before
        it is returned to user code.
        """
        return response

    def pre_list_debuggees(
        self,
        request: debugger.ListDebuggeesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[debugger.ListDebuggeesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_debuggees

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Debugger2 server.
        """
        return request, metadata

    def post_list_debuggees(
        self, response: debugger.ListDebuggeesResponse
    ) -> debugger.ListDebuggeesResponse:
        """Post-rpc interceptor for list_debuggees

        Override in a subclass to manipulate the response
        after it is returned by the Debugger2 server but before
        it is returned to user code.
        """
        return response

    def pre_set_breakpoint(
        self,
        request: debugger.SetBreakpointRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[debugger.SetBreakpointRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for set_breakpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Debugger2 server.
        """
        return request, metadata

    def post_set_breakpoint(
        self, response: debugger.SetBreakpointResponse
    ) -> debugger.SetBreakpointResponse:
        """Post-rpc interceptor for set_breakpoint

        Override in a subclass to manipulate the response
        after it is returned by the Debugger2 server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class Debugger2RestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: Debugger2RestInterceptor


class Debugger2RestTransport(Debugger2Transport):
    """REST backend transport for Debugger2.

    The Debugger service provides the API that allows users to
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

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(
        self,
        *,
        host: str = "clouddebugger.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[Debugger2RestInterceptor] = None,
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
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or Debugger2RestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _DeleteBreakpoint(Debugger2RestStub):
        def __hash__(self):
            return hash("DeleteBreakpoint")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "clientVersion": "",
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: debugger.DeleteBreakpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ):
            r"""Call the delete breakpoint method over HTTP.

            Args:
                request (~.debugger.DeleteBreakpointRequest):
                    The request object. Request to delete a breakpoint.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/debugger/debuggees/{debuggee_id}/breakpoints/{breakpoint_id}",
                },
            ]
            request, metadata = self._interceptor.pre_delete_breakpoint(
                request, metadata
            )
            pb_request = debugger.DeleteBreakpointRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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

    class _GetBreakpoint(Debugger2RestStub):
        def __hash__(self):
            return hash("GetBreakpoint")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "clientVersion": "",
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: debugger.GetBreakpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> debugger.GetBreakpointResponse:
            r"""Call the get breakpoint method over HTTP.

            Args:
                request (~.debugger.GetBreakpointRequest):
                    The request object. Request to get breakpoint
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.debugger.GetBreakpointResponse:
                    Response for getting breakpoint
                information.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/debugger/debuggees/{debuggee_id}/breakpoints/{breakpoint_id}",
                },
            ]
            request, metadata = self._interceptor.pre_get_breakpoint(request, metadata)
            pb_request = debugger.GetBreakpointRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
            resp = debugger.GetBreakpointResponse()
            pb_resp = debugger.GetBreakpointResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_breakpoint(resp)
            return resp

    class _ListBreakpoints(Debugger2RestStub):
        def __hash__(self):
            return hash("ListBreakpoints")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "clientVersion": "",
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: debugger.ListBreakpointsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> debugger.ListBreakpointsResponse:
            r"""Call the list breakpoints method over HTTP.

            Args:
                request (~.debugger.ListBreakpointsRequest):
                    The request object. Request to list breakpoints.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.debugger.ListBreakpointsResponse:
                    Response for listing breakpoints.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/debugger/debuggees/{debuggee_id}/breakpoints",
                },
            ]
            request, metadata = self._interceptor.pre_list_breakpoints(
                request, metadata
            )
            pb_request = debugger.ListBreakpointsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
            resp = debugger.ListBreakpointsResponse()
            pb_resp = debugger.ListBreakpointsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_breakpoints(resp)
            return resp

    class _ListDebuggees(Debugger2RestStub):
        def __hash__(self):
            return hash("ListDebuggees")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "project": "",
            "clientVersion": "",
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: debugger.ListDebuggeesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> debugger.ListDebuggeesResponse:
            r"""Call the list debuggees method over HTTP.

            Args:
                request (~.debugger.ListDebuggeesRequest):
                    The request object. Request to list debuggees.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.debugger.ListDebuggeesResponse:
                    Response for listing debuggees.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/debugger/debuggees",
                },
            ]
            request, metadata = self._interceptor.pre_list_debuggees(request, metadata)
            pb_request = debugger.ListDebuggeesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
            resp = debugger.ListDebuggeesResponse()
            pb_resp = debugger.ListDebuggeesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_debuggees(resp)
            return resp

    class _SetBreakpoint(Debugger2RestStub):
        def __hash__(self):
            return hash("SetBreakpoint")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "breakpoint": {},
            "clientVersion": "",
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: debugger.SetBreakpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> debugger.SetBreakpointResponse:
            r"""Call the set breakpoint method over HTTP.

            Args:
                request (~.debugger.SetBreakpointRequest):
                    The request object. Request to set a breakpoint
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.debugger.SetBreakpointResponse:
                    Response for setting a breakpoint.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/debugger/debuggees/{debuggee_id}/breakpoints/set",
                    "body": "breakpoint_",
                },
            ]
            request, metadata = self._interceptor.pre_set_breakpoint(request, metadata)
            pb_request = debugger.SetBreakpointRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
            resp = debugger.SetBreakpointResponse()
            pb_resp = debugger.SetBreakpointResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_set_breakpoint(resp)
            return resp

    @property
    def delete_breakpoint(
        self,
    ) -> Callable[[debugger.DeleteBreakpointRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBreakpoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_breakpoint(
        self,
    ) -> Callable[[debugger.GetBreakpointRequest], debugger.GetBreakpointResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBreakpoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_breakpoints(
        self,
    ) -> Callable[[debugger.ListBreakpointsRequest], debugger.ListBreakpointsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBreakpoints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_debuggees(
        self,
    ) -> Callable[[debugger.ListDebuggeesRequest], debugger.ListDebuggeesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDebuggees(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_breakpoint(
        self,
    ) -> Callable[[debugger.SetBreakpointRequest], debugger.SetBreakpointResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetBreakpoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("Debugger2RestTransport",)
