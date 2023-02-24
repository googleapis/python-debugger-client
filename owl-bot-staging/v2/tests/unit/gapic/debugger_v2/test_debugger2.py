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
import os
# try/except added for compatibility with python < 3.8
try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    import mock

import grpc
from grpc.experimental import aio
from collections.abc import Iterable
from google.protobuf import json_format
import json
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule
from proto.marshal.rules import wrappers
from requests import Response
from requests import Request, PreparedRequest
from requests.sessions import Session
from google.protobuf import json_format

from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import path_template
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.debugger_v2.services.debugger2 import Debugger2AsyncClient
from google.cloud.debugger_v2.services.debugger2 import Debugger2Client
from google.cloud.debugger_v2.services.debugger2 import transports
from google.cloud.debugger_v2.types import data
from google.cloud.debugger_v2.types import debugger
from google.oauth2 import service_account
from google.protobuf import timestamp_pb2  # type: ignore
from google.protobuf import wrappers_pb2  # type: ignore
import google.auth


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return "foo.googleapis.com" if ("localhost" in client.DEFAULT_ENDPOINT) else client.DEFAULT_ENDPOINT


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert Debugger2Client._get_default_mtls_endpoint(None) is None
    assert Debugger2Client._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert Debugger2Client._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    assert Debugger2Client._get_default_mtls_endpoint(sandbox_endpoint) == sandbox_mtls_endpoint
    assert Debugger2Client._get_default_mtls_endpoint(sandbox_mtls_endpoint) == sandbox_mtls_endpoint
    assert Debugger2Client._get_default_mtls_endpoint(non_googleapi) == non_googleapi


@pytest.mark.parametrize("client_class,transport_name", [
    (Debugger2Client, "grpc"),
    (Debugger2AsyncClient, "grpc_asyncio"),
    (Debugger2Client, "rest"),
])
def test_debugger2_client_from_service_account_info(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_info') as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'clouddebugger.googleapis.com:443'
            if transport_name in ['grpc', 'grpc_asyncio']
            else
            'https://clouddebugger.googleapis.com'
        )


@pytest.mark.parametrize("transport_class,transport_name", [
    (transports.Debugger2GrpcTransport, "grpc"),
    (transports.Debugger2GrpcAsyncIOTransport, "grpc_asyncio"),
    (transports.Debugger2RestTransport, "rest"),
])
def test_debugger2_client_service_account_always_use_jwt(transport_class, transport_name):
    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize("client_class,transport_name", [
    (Debugger2Client, "grpc"),
    (Debugger2AsyncClient, "grpc_asyncio"),
    (Debugger2Client, "rest"),
])
def test_debugger2_client_from_service_account_file(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'clouddebugger.googleapis.com:443'
            if transport_name in ['grpc', 'grpc_asyncio']
            else
            'https://clouddebugger.googleapis.com'
        )


def test_debugger2_client_get_transport_class():
    transport = Debugger2Client.get_transport_class()
    available_transports = [
        transports.Debugger2GrpcTransport,
        transports.Debugger2RestTransport,
    ]
    assert transport in available_transports

    transport = Debugger2Client.get_transport_class("grpc")
    assert transport == transports.Debugger2GrpcTransport


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (Debugger2Client, transports.Debugger2GrpcTransport, "grpc"),
    (Debugger2AsyncClient, transports.Debugger2GrpcAsyncIOTransport, "grpc_asyncio"),
    (Debugger2Client, transports.Debugger2RestTransport, "rest"),
])
@mock.patch.object(Debugger2Client, "DEFAULT_ENDPOINT", modify_default_endpoint(Debugger2Client))
@mock.patch.object(Debugger2AsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(Debugger2AsyncClient))
def test_debugger2_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(Debugger2Client, 'get_transport_class') as gtc:
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials()
        )
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(Debugger2Client, 'get_transport_class') as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class(transport=transport_name)

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}):
        with pytest.raises(ValueError):
            client = client_class(transport=transport_name)

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )
    # Check the case api_endpoint is provided
    options = client_options.ClientOptions(api_audience="https://language.googleapis.com")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience="https://language.googleapis.com"
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,use_client_cert_env", [
    (Debugger2Client, transports.Debugger2GrpcTransport, "grpc", "true"),
    (Debugger2AsyncClient, transports.Debugger2GrpcAsyncIOTransport, "grpc_asyncio", "true"),
    (Debugger2Client, transports.Debugger2GrpcTransport, "grpc", "false"),
    (Debugger2AsyncClient, transports.Debugger2GrpcAsyncIOTransport, "grpc_asyncio", "false"),
    (Debugger2Client, transports.Debugger2RestTransport, "rest", "true"),
    (Debugger2Client, transports.Debugger2RestTransport, "rest", "false"),
])
@mock.patch.object(Debugger2Client, "DEFAULT_ENDPOINT", modify_default_endpoint(Debugger2Client))
@mock.patch.object(Debugger2AsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(Debugger2AsyncClient))
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_debugger2_client_mtls_env_auto(client_class, transport_class, transport_name, use_client_cert_env):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        options = client_options.ClientOptions(client_cert_source=client_cert_source_callback)
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
                with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=client_cert_source_callback):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                        api_audience=None,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch("google.auth.transport.mtls.has_default_client_cert_source", return_value=False):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                    api_audience=None,
                )


@pytest.mark.parametrize("client_class", [
    Debugger2Client, Debugger2AsyncClient
])
@mock.patch.object(Debugger2Client, "DEFAULT_ENDPOINT", modify_default_endpoint(Debugger2Client))
@mock.patch.object(Debugger2AsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(Debugger2AsyncClient))
def test_debugger2_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=False):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
            with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=mock_client_cert_source):
                api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (Debugger2Client, transports.Debugger2GrpcTransport, "grpc"),
    (Debugger2AsyncClient, transports.Debugger2GrpcAsyncIOTransport, "grpc_asyncio"),
    (Debugger2Client, transports.Debugger2RestTransport, "rest"),
])
def test_debugger2_client_client_options_scopes(client_class, transport_class, transport_name):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (Debugger2Client, transports.Debugger2GrpcTransport, "grpc", grpc_helpers),
    (Debugger2AsyncClient, transports.Debugger2GrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
    (Debugger2Client, transports.Debugger2RestTransport, "rest", None),
])
def test_debugger2_client_client_options_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

def test_debugger2_client_client_options_from_dict():
    with mock.patch('google.cloud.debugger_v2.services.debugger2.transports.Debugger2GrpcTransport.__init__') as grpc_transport:
        grpc_transport.return_value = None
        client = Debugger2Client(
            client_options={'api_endpoint': 'squid.clam.whelk'}
        )
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (Debugger2Client, transports.Debugger2GrpcTransport, "grpc", grpc_helpers),
    (Debugger2AsyncClient, transports.Debugger2GrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
])
def test_debugger2_client_create_channel_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "clouddebugger.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                'https://www.googleapis.com/auth/cloud-platform',
                'https://www.googleapis.com/auth/cloud_debugger',
),
            scopes=None,
            default_host="clouddebugger.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("request_type", [
  debugger.SetBreakpointRequest,
  dict,
])
def test_set_breakpoint(request_type, transport: str = 'grpc'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.set_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.SetBreakpointResponse(
        )
        response = client.set_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.SetBreakpointRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.SetBreakpointResponse)


def test_set_breakpoint_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.set_breakpoint),
            '__call__') as call:
        client.set_breakpoint()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.SetBreakpointRequest()

@pytest.mark.asyncio
async def test_set_breakpoint_async(transport: str = 'grpc_asyncio', request_type=debugger.SetBreakpointRequest):
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.set_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(debugger.SetBreakpointResponse(
        ))
        response = await client.set_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.SetBreakpointRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.SetBreakpointResponse)


@pytest.mark.asyncio
async def test_set_breakpoint_async_from_dict():
    await test_set_breakpoint_async(request_type=dict)


def test_set_breakpoint_field_headers():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = debugger.SetBreakpointRequest()

    request.debuggee_id = 'debuggee_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.set_breakpoint),
            '__call__') as call:
        call.return_value = debugger.SetBreakpointResponse()
        client.set_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'debuggee_id=debuggee_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_set_breakpoint_field_headers_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = debugger.SetBreakpointRequest()

    request.debuggee_id = 'debuggee_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.set_breakpoint),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(debugger.SetBreakpointResponse())
        await client.set_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'debuggee_id=debuggee_id_value',
    ) in kw['metadata']


def test_set_breakpoint_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.set_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.SetBreakpointResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.set_breakpoint(
            debuggee_id='debuggee_id_value',
            breakpoint_=data.Breakpoint(id='id_value'),
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].debuggee_id
        mock_val = 'debuggee_id_value'
        assert arg == mock_val
        arg = args[0].breakpoint_
        mock_val = data.Breakpoint(id='id_value')
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val


def test_set_breakpoint_flattened_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_breakpoint(
            debugger.SetBreakpointRequest(),
            debuggee_id='debuggee_id_value',
            breakpoint_=data.Breakpoint(id='id_value'),
            client_version='client_version_value',
        )

@pytest.mark.asyncio
async def test_set_breakpoint_flattened_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.set_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.SetBreakpointResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(debugger.SetBreakpointResponse())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.set_breakpoint(
            debuggee_id='debuggee_id_value',
            breakpoint_=data.Breakpoint(id='id_value'),
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].debuggee_id
        mock_val = 'debuggee_id_value'
        assert arg == mock_val
        arg = args[0].breakpoint_
        mock_val = data.Breakpoint(id='id_value')
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val

@pytest.mark.asyncio
async def test_set_breakpoint_flattened_error_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.set_breakpoint(
            debugger.SetBreakpointRequest(),
            debuggee_id='debuggee_id_value',
            breakpoint_=data.Breakpoint(id='id_value'),
            client_version='client_version_value',
        )


@pytest.mark.parametrize("request_type", [
  debugger.GetBreakpointRequest,
  dict,
])
def test_get_breakpoint(request_type, transport: str = 'grpc'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.GetBreakpointResponse(
        )
        response = client.get_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.GetBreakpointRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.GetBreakpointResponse)


def test_get_breakpoint_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_breakpoint),
            '__call__') as call:
        client.get_breakpoint()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.GetBreakpointRequest()

@pytest.mark.asyncio
async def test_get_breakpoint_async(transport: str = 'grpc_asyncio', request_type=debugger.GetBreakpointRequest):
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(debugger.GetBreakpointResponse(
        ))
        response = await client.get_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.GetBreakpointRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.GetBreakpointResponse)


@pytest.mark.asyncio
async def test_get_breakpoint_async_from_dict():
    await test_get_breakpoint_async(request_type=dict)


def test_get_breakpoint_field_headers():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = debugger.GetBreakpointRequest()

    request.debuggee_id = 'debuggee_id_value'
    request.breakpoint_id = 'breakpoint_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_breakpoint),
            '__call__') as call:
        call.return_value = debugger.GetBreakpointResponse()
        client.get_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'debuggee_id=debuggee_id_value&breakpoint_id=breakpoint_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_get_breakpoint_field_headers_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = debugger.GetBreakpointRequest()

    request.debuggee_id = 'debuggee_id_value'
    request.breakpoint_id = 'breakpoint_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_breakpoint),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(debugger.GetBreakpointResponse())
        await client.get_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'debuggee_id=debuggee_id_value&breakpoint_id=breakpoint_id_value',
    ) in kw['metadata']


def test_get_breakpoint_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.GetBreakpointResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_breakpoint(
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].debuggee_id
        mock_val = 'debuggee_id_value'
        assert arg == mock_val
        arg = args[0].breakpoint_id
        mock_val = 'breakpoint_id_value'
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val


def test_get_breakpoint_flattened_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_breakpoint(
            debugger.GetBreakpointRequest(),
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )

@pytest.mark.asyncio
async def test_get_breakpoint_flattened_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.GetBreakpointResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(debugger.GetBreakpointResponse())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_breakpoint(
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].debuggee_id
        mock_val = 'debuggee_id_value'
        assert arg == mock_val
        arg = args[0].breakpoint_id
        mock_val = 'breakpoint_id_value'
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val

@pytest.mark.asyncio
async def test_get_breakpoint_flattened_error_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_breakpoint(
            debugger.GetBreakpointRequest(),
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )


@pytest.mark.parametrize("request_type", [
  debugger.DeleteBreakpointRequest,
  dict,
])
def test_delete_breakpoint(request_type, transport: str = 'grpc'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.DeleteBreakpointRequest()

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_breakpoint_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_breakpoint),
            '__call__') as call:
        client.delete_breakpoint()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.DeleteBreakpointRequest()

@pytest.mark.asyncio
async def test_delete_breakpoint_async(transport: str = 'grpc_asyncio', request_type=debugger.DeleteBreakpointRequest):
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.DeleteBreakpointRequest()

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_delete_breakpoint_async_from_dict():
    await test_delete_breakpoint_async(request_type=dict)


def test_delete_breakpoint_field_headers():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = debugger.DeleteBreakpointRequest()

    request.debuggee_id = 'debuggee_id_value'
    request.breakpoint_id = 'breakpoint_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_breakpoint),
            '__call__') as call:
        call.return_value = None
        client.delete_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'debuggee_id=debuggee_id_value&breakpoint_id=breakpoint_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_delete_breakpoint_field_headers_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = debugger.DeleteBreakpointRequest()

    request.debuggee_id = 'debuggee_id_value'
    request.breakpoint_id = 'breakpoint_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_breakpoint),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_breakpoint(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'debuggee_id=debuggee_id_value&breakpoint_id=breakpoint_id_value',
    ) in kw['metadata']


def test_delete_breakpoint_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_breakpoint(
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].debuggee_id
        mock_val = 'debuggee_id_value'
        assert arg == mock_val
        arg = args[0].breakpoint_id
        mock_val = 'breakpoint_id_value'
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val


def test_delete_breakpoint_flattened_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_breakpoint(
            debugger.DeleteBreakpointRequest(),
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )

@pytest.mark.asyncio
async def test_delete_breakpoint_flattened_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_breakpoint),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_breakpoint(
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].debuggee_id
        mock_val = 'debuggee_id_value'
        assert arg == mock_val
        arg = args[0].breakpoint_id
        mock_val = 'breakpoint_id_value'
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val

@pytest.mark.asyncio
async def test_delete_breakpoint_flattened_error_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_breakpoint(
            debugger.DeleteBreakpointRequest(),
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )


@pytest.mark.parametrize("request_type", [
  debugger.ListBreakpointsRequest,
  dict,
])
def test_list_breakpoints(request_type, transport: str = 'grpc'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_breakpoints),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.ListBreakpointsResponse(
            next_wait_token='next_wait_token_value',
        )
        response = client.list_breakpoints(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.ListBreakpointsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.ListBreakpointsResponse)
    assert response.next_wait_token == 'next_wait_token_value'


def test_list_breakpoints_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_breakpoints),
            '__call__') as call:
        client.list_breakpoints()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.ListBreakpointsRequest()

@pytest.mark.asyncio
async def test_list_breakpoints_async(transport: str = 'grpc_asyncio', request_type=debugger.ListBreakpointsRequest):
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_breakpoints),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(debugger.ListBreakpointsResponse(
            next_wait_token='next_wait_token_value',
        ))
        response = await client.list_breakpoints(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.ListBreakpointsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.ListBreakpointsResponse)
    assert response.next_wait_token == 'next_wait_token_value'


@pytest.mark.asyncio
async def test_list_breakpoints_async_from_dict():
    await test_list_breakpoints_async(request_type=dict)


def test_list_breakpoints_field_headers():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = debugger.ListBreakpointsRequest()

    request.debuggee_id = 'debuggee_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_breakpoints),
            '__call__') as call:
        call.return_value = debugger.ListBreakpointsResponse()
        client.list_breakpoints(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'debuggee_id=debuggee_id_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_list_breakpoints_field_headers_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = debugger.ListBreakpointsRequest()

    request.debuggee_id = 'debuggee_id_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_breakpoints),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(debugger.ListBreakpointsResponse())
        await client.list_breakpoints(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'debuggee_id=debuggee_id_value',
    ) in kw['metadata']


def test_list_breakpoints_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_breakpoints),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.ListBreakpointsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_breakpoints(
            debuggee_id='debuggee_id_value',
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].debuggee_id
        mock_val = 'debuggee_id_value'
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val


def test_list_breakpoints_flattened_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_breakpoints(
            debugger.ListBreakpointsRequest(),
            debuggee_id='debuggee_id_value',
            client_version='client_version_value',
        )

@pytest.mark.asyncio
async def test_list_breakpoints_flattened_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_breakpoints),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.ListBreakpointsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(debugger.ListBreakpointsResponse())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_breakpoints(
            debuggee_id='debuggee_id_value',
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].debuggee_id
        mock_val = 'debuggee_id_value'
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val

@pytest.mark.asyncio
async def test_list_breakpoints_flattened_error_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_breakpoints(
            debugger.ListBreakpointsRequest(),
            debuggee_id='debuggee_id_value',
            client_version='client_version_value',
        )


@pytest.mark.parametrize("request_type", [
  debugger.ListDebuggeesRequest,
  dict,
])
def test_list_debuggees(request_type, transport: str = 'grpc'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_debuggees),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.ListDebuggeesResponse(
        )
        response = client.list_debuggees(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.ListDebuggeesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.ListDebuggeesResponse)


def test_list_debuggees_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_debuggees),
            '__call__') as call:
        client.list_debuggees()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.ListDebuggeesRequest()

@pytest.mark.asyncio
async def test_list_debuggees_async(transport: str = 'grpc_asyncio', request_type=debugger.ListDebuggeesRequest):
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_debuggees),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(debugger.ListDebuggeesResponse(
        ))
        response = await client.list_debuggees(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == debugger.ListDebuggeesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.ListDebuggeesResponse)


@pytest.mark.asyncio
async def test_list_debuggees_async_from_dict():
    await test_list_debuggees_async(request_type=dict)


def test_list_debuggees_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_debuggees),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.ListDebuggeesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_debuggees(
            project='project_value',
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project
        mock_val = 'project_value'
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val


def test_list_debuggees_flattened_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_debuggees(
            debugger.ListDebuggeesRequest(),
            project='project_value',
            client_version='client_version_value',
        )

@pytest.mark.asyncio
async def test_list_debuggees_flattened_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_debuggees),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = debugger.ListDebuggeesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(debugger.ListDebuggeesResponse())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_debuggees(
            project='project_value',
            client_version='client_version_value',
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project
        mock_val = 'project_value'
        assert arg == mock_val
        arg = args[0].client_version
        mock_val = 'client_version_value'
        assert arg == mock_val

@pytest.mark.asyncio
async def test_list_debuggees_flattened_error_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_debuggees(
            debugger.ListDebuggeesRequest(),
            project='project_value',
            client_version='client_version_value',
        )


@pytest.mark.parametrize("request_type", [
    debugger.SetBreakpointRequest,
    dict,
])
def test_set_breakpoint_rest(request_type):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {'debuggee_id': 'sample1'}
    request_init["breakpoint_"] = {'id': 'id_value', 'action': 1, 'location': {'path': 'path_value', 'line': 424, 'column': 654}, 'condition': 'condition_value', 'expressions': ['expressions_value1', 'expressions_value2'], 'log_message_format': 'log_message_format_value', 'log_level': 1, 'is_final_state': True, 'create_time': {'seconds': 751, 'nanos': 543}, 'final_time': {}, 'user_email': 'user_email_value', 'status': {'is_error': True, 'refers_to': 3, 'description': {'format_': 'format__value', 'parameters': ['parameters_value1', 'parameters_value2']}}, 'stack_frames': [{'function': 'function_value', 'location': {}, 'arguments': [{'name': 'name_value', 'value': 'value_value', 'type_': 'type__value', 'members': {}, 'var_table_index': {'value': 541}, 'status': {}}], 'locals_': {}}], 'evaluated_expressions': {}, 'variable_table': {}, 'labels': {}}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = debugger.SetBreakpointResponse(
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = debugger.SetBreakpointResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        response = client.set_breakpoint(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.SetBreakpointResponse)


def test_set_breakpoint_rest_required_fields(request_type=debugger.SetBreakpointRequest):
    transport_class = transports.Debugger2RestTransport

    request_init = {}
    request_init["debuggee_id"] = ""
    request_init["client_version"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(json_format.MessageToJson(
        pb_request,
        including_default_value_fields=False,
        use_integers_for_enums=False
    ))

    # verify fields with default values are dropped
    assert "clientVersion" not in jsonified_request

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).set_breakpoint._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == request_init["client_version"]

    jsonified_request["debuggeeId"] = 'debuggee_id_value'
    jsonified_request["clientVersion"] = 'client_version_value'

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).set_breakpoint._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("breakpoint_", "client_version", ))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "debuggeeId" in jsonified_request
    assert jsonified_request["debuggeeId"] == 'debuggee_id_value'
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == 'client_version_value'

    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest',
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = debugger.SetBreakpointResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, 'transcode') as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                'uri': 'v1/sample_method',
                'method': "post",
                'query_params': pb_request,
            }
            transcode_result['body'] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = debugger.SetBreakpointResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode('UTF-8')
            req.return_value = response_value

            response = client.set_breakpoint(request)

            expected_params = [
                (
                    "clientVersion",
                    "",
                ),
                ('$alt', 'json;enum-encoding=int')
            ]
            actual_params = req.call_args.kwargs['params']
            assert expected_params == actual_params


def test_set_breakpoint_rest_unset_required_fields():
    transport = transports.Debugger2RestTransport(credentials=ga_credentials.AnonymousCredentials)

    unset_fields = transport.set_breakpoint._get_unset_required_fields({})
    assert set(unset_fields) == (set(("breakpoint", "clientVersion", )) & set(("debuggeeId", "breakpoint", "clientVersion", )))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_set_breakpoint_rest_interceptors(null_interceptor):
    transport = transports.Debugger2RestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.Debugger2RestInterceptor(),
        )
    client = Debugger2Client(transport=transport)
    with mock.patch.object(type(client.transport._session), "request") as req, \
         mock.patch.object(path_template, "transcode")  as transcode, \
         mock.patch.object(transports.Debugger2RestInterceptor, "post_set_breakpoint") as post, \
         mock.patch.object(transports.Debugger2RestInterceptor, "pre_set_breakpoint") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = debugger.SetBreakpointRequest.pb(debugger.SetBreakpointRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = debugger.SetBreakpointResponse.to_json(debugger.SetBreakpointResponse())

        request = debugger.SetBreakpointRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = debugger.SetBreakpointResponse()

        client.set_breakpoint(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()


def test_set_breakpoint_rest_bad_request(transport: str = 'rest', request_type=debugger.SetBreakpointRequest):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {'debuggee_id': 'sample1'}
    request_init["breakpoint_"] = {'id': 'id_value', 'action': 1, 'location': {'path': 'path_value', 'line': 424, 'column': 654}, 'condition': 'condition_value', 'expressions': ['expressions_value1', 'expressions_value2'], 'log_message_format': 'log_message_format_value', 'log_level': 1, 'is_final_state': True, 'create_time': {'seconds': 751, 'nanos': 543}, 'final_time': {}, 'user_email': 'user_email_value', 'status': {'is_error': True, 'refers_to': 3, 'description': {'format_': 'format__value', 'parameters': ['parameters_value1', 'parameters_value2']}}, 'stack_frames': [{'function': 'function_value', 'location': {}, 'arguments': [{'name': 'name_value', 'value': 'value_value', 'type_': 'type__value', 'members': {}, 'var_table_index': {'value': 541}, 'status': {}}], 'locals_': {}}], 'evaluated_expressions': {}, 'variable_table': {}, 'labels': {}}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.set_breakpoint(request)


def test_set_breakpoint_rest_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = debugger.SetBreakpointResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {'debuggee_id': 'sample1'}

        # get truthy value for each flattened field
        mock_args = dict(
            debuggee_id='debuggee_id_value',
            breakpoint_=data.Breakpoint(id='id_value'),
            client_version='client_version_value',
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = debugger.SetBreakpointResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value

        client.set_breakpoint(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate("%s/v2/debugger/debuggees/{debuggee_id}/breakpoints/set" % client.transport._host, args[1])


def test_set_breakpoint_rest_flattened_error(transport: str = 'rest'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_breakpoint(
            debugger.SetBreakpointRequest(),
            debuggee_id='debuggee_id_value',
            breakpoint_=data.Breakpoint(id='id_value'),
            client_version='client_version_value',
        )


def test_set_breakpoint_rest_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest'
    )


@pytest.mark.parametrize("request_type", [
    debugger.GetBreakpointRequest,
    dict,
])
def test_get_breakpoint_rest(request_type):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {'debuggee_id': 'sample1', 'breakpoint_id': 'sample2'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = debugger.GetBreakpointResponse(
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = debugger.GetBreakpointResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        response = client.get_breakpoint(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.GetBreakpointResponse)


def test_get_breakpoint_rest_required_fields(request_type=debugger.GetBreakpointRequest):
    transport_class = transports.Debugger2RestTransport

    request_init = {}
    request_init["debuggee_id"] = ""
    request_init["breakpoint_id"] = ""
    request_init["client_version"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(json_format.MessageToJson(
        pb_request,
        including_default_value_fields=False,
        use_integers_for_enums=False
    ))

    # verify fields with default values are dropped
    assert "clientVersion" not in jsonified_request

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).get_breakpoint._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == request_init["client_version"]

    jsonified_request["debuggeeId"] = 'debuggee_id_value'
    jsonified_request["breakpointId"] = 'breakpoint_id_value'
    jsonified_request["clientVersion"] = 'client_version_value'

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).get_breakpoint._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("client_version", ))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "debuggeeId" in jsonified_request
    assert jsonified_request["debuggeeId"] == 'debuggee_id_value'
    assert "breakpointId" in jsonified_request
    assert jsonified_request["breakpointId"] == 'breakpoint_id_value'
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == 'client_version_value'

    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest',
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = debugger.GetBreakpointResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, 'transcode') as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                'uri': 'v1/sample_method',
                'method': "get",
                'query_params': pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = debugger.GetBreakpointResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode('UTF-8')
            req.return_value = response_value

            response = client.get_breakpoint(request)

            expected_params = [
                (
                    "clientVersion",
                    "",
                ),
                ('$alt', 'json;enum-encoding=int')
            ]
            actual_params = req.call_args.kwargs['params']
            assert expected_params == actual_params


def test_get_breakpoint_rest_unset_required_fields():
    transport = transports.Debugger2RestTransport(credentials=ga_credentials.AnonymousCredentials)

    unset_fields = transport.get_breakpoint._get_unset_required_fields({})
    assert set(unset_fields) == (set(("clientVersion", )) & set(("debuggeeId", "breakpointId", "clientVersion", )))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_breakpoint_rest_interceptors(null_interceptor):
    transport = transports.Debugger2RestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.Debugger2RestInterceptor(),
        )
    client = Debugger2Client(transport=transport)
    with mock.patch.object(type(client.transport._session), "request") as req, \
         mock.patch.object(path_template, "transcode")  as transcode, \
         mock.patch.object(transports.Debugger2RestInterceptor, "post_get_breakpoint") as post, \
         mock.patch.object(transports.Debugger2RestInterceptor, "pre_get_breakpoint") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = debugger.GetBreakpointRequest.pb(debugger.GetBreakpointRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = debugger.GetBreakpointResponse.to_json(debugger.GetBreakpointResponse())

        request = debugger.GetBreakpointRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = debugger.GetBreakpointResponse()

        client.get_breakpoint(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()


def test_get_breakpoint_rest_bad_request(transport: str = 'rest', request_type=debugger.GetBreakpointRequest):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {'debuggee_id': 'sample1', 'breakpoint_id': 'sample2'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_breakpoint(request)


def test_get_breakpoint_rest_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = debugger.GetBreakpointResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {'debuggee_id': 'sample1', 'breakpoint_id': 'sample2'}

        # get truthy value for each flattened field
        mock_args = dict(
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = debugger.GetBreakpointResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value

        client.get_breakpoint(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate("%s/v2/debugger/debuggees/{debuggee_id}/breakpoints/{breakpoint_id}" % client.transport._host, args[1])


def test_get_breakpoint_rest_flattened_error(transport: str = 'rest'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_breakpoint(
            debugger.GetBreakpointRequest(),
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )


def test_get_breakpoint_rest_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest'
    )


@pytest.mark.parametrize("request_type", [
    debugger.DeleteBreakpointRequest,
    dict,
])
def test_delete_breakpoint_rest(request_type):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {'debuggee_id': 'sample1', 'breakpoint_id': 'sample2'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = ''

        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        response = client.delete_breakpoint(request)

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_breakpoint_rest_required_fields(request_type=debugger.DeleteBreakpointRequest):
    transport_class = transports.Debugger2RestTransport

    request_init = {}
    request_init["debuggee_id"] = ""
    request_init["breakpoint_id"] = ""
    request_init["client_version"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(json_format.MessageToJson(
        pb_request,
        including_default_value_fields=False,
        use_integers_for_enums=False
    ))

    # verify fields with default values are dropped
    assert "clientVersion" not in jsonified_request

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).delete_breakpoint._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == request_init["client_version"]

    jsonified_request["debuggeeId"] = 'debuggee_id_value'
    jsonified_request["breakpointId"] = 'breakpoint_id_value'
    jsonified_request["clientVersion"] = 'client_version_value'

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).delete_breakpoint._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("client_version", ))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "debuggeeId" in jsonified_request
    assert jsonified_request["debuggeeId"] == 'debuggee_id_value'
    assert "breakpointId" in jsonified_request
    assert jsonified_request["breakpointId"] == 'breakpoint_id_value'
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == 'client_version_value'

    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest',
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = None
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, 'transcode') as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                'uri': 'v1/sample_method',
                'method': "delete",
                'query_params': pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = ''

            response_value._content = json_return_value.encode('UTF-8')
            req.return_value = response_value

            response = client.delete_breakpoint(request)

            expected_params = [
                (
                    "clientVersion",
                    "",
                ),
                ('$alt', 'json;enum-encoding=int')
            ]
            actual_params = req.call_args.kwargs['params']
            assert expected_params == actual_params


def test_delete_breakpoint_rest_unset_required_fields():
    transport = transports.Debugger2RestTransport(credentials=ga_credentials.AnonymousCredentials)

    unset_fields = transport.delete_breakpoint._get_unset_required_fields({})
    assert set(unset_fields) == (set(("clientVersion", )) & set(("debuggeeId", "breakpointId", "clientVersion", )))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_breakpoint_rest_interceptors(null_interceptor):
    transport = transports.Debugger2RestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.Debugger2RestInterceptor(),
        )
    client = Debugger2Client(transport=transport)
    with mock.patch.object(type(client.transport._session), "request") as req, \
         mock.patch.object(path_template, "transcode")  as transcode, \
         mock.patch.object(transports.Debugger2RestInterceptor, "pre_delete_breakpoint") as pre:
        pre.assert_not_called()
        pb_message = debugger.DeleteBreakpointRequest.pb(debugger.DeleteBreakpointRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()

        request = debugger.DeleteBreakpointRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_breakpoint(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()


def test_delete_breakpoint_rest_bad_request(transport: str = 'rest', request_type=debugger.DeleteBreakpointRequest):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {'debuggee_id': 'sample1', 'breakpoint_id': 'sample2'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.delete_breakpoint(request)


def test_delete_breakpoint_rest_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # get arguments that satisfy an http rule for this method
        sample_request = {'debuggee_id': 'sample1', 'breakpoint_id': 'sample2'}

        # get truthy value for each flattened field
        mock_args = dict(
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = ''
        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value

        client.delete_breakpoint(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate("%s/v2/debugger/debuggees/{debuggee_id}/breakpoints/{breakpoint_id}" % client.transport._host, args[1])


def test_delete_breakpoint_rest_flattened_error(transport: str = 'rest'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_breakpoint(
            debugger.DeleteBreakpointRequest(),
            debuggee_id='debuggee_id_value',
            breakpoint_id='breakpoint_id_value',
            client_version='client_version_value',
        )


def test_delete_breakpoint_rest_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest'
    )


@pytest.mark.parametrize("request_type", [
    debugger.ListBreakpointsRequest,
    dict,
])
def test_list_breakpoints_rest(request_type):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {'debuggee_id': 'sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = debugger.ListBreakpointsResponse(
              next_wait_token='next_wait_token_value',
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = debugger.ListBreakpointsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        response = client.list_breakpoints(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.ListBreakpointsResponse)
    assert response.next_wait_token == 'next_wait_token_value'


def test_list_breakpoints_rest_required_fields(request_type=debugger.ListBreakpointsRequest):
    transport_class = transports.Debugger2RestTransport

    request_init = {}
    request_init["debuggee_id"] = ""
    request_init["client_version"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(json_format.MessageToJson(
        pb_request,
        including_default_value_fields=False,
        use_integers_for_enums=False
    ))

    # verify fields with default values are dropped
    assert "clientVersion" not in jsonified_request

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).list_breakpoints._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == request_init["client_version"]

    jsonified_request["debuggeeId"] = 'debuggee_id_value'
    jsonified_request["clientVersion"] = 'client_version_value'

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).list_breakpoints._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("action", "client_version", "include_all_users", "include_inactive", "strip_results", "wait_token", ))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "debuggeeId" in jsonified_request
    assert jsonified_request["debuggeeId"] == 'debuggee_id_value'
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == 'client_version_value'

    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest',
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = debugger.ListBreakpointsResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, 'transcode') as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                'uri': 'v1/sample_method',
                'method': "get",
                'query_params': pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = debugger.ListBreakpointsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode('UTF-8')
            req.return_value = response_value

            response = client.list_breakpoints(request)

            expected_params = [
                (
                    "clientVersion",
                    "",
                ),
                ('$alt', 'json;enum-encoding=int')
            ]
            actual_params = req.call_args.kwargs['params']
            assert expected_params == actual_params


def test_list_breakpoints_rest_unset_required_fields():
    transport = transports.Debugger2RestTransport(credentials=ga_credentials.AnonymousCredentials)

    unset_fields = transport.list_breakpoints._get_unset_required_fields({})
    assert set(unset_fields) == (set(("action", "clientVersion", "includeAllUsers", "includeInactive", "stripResults", "waitToken", )) & set(("debuggeeId", "clientVersion", )))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_breakpoints_rest_interceptors(null_interceptor):
    transport = transports.Debugger2RestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.Debugger2RestInterceptor(),
        )
    client = Debugger2Client(transport=transport)
    with mock.patch.object(type(client.transport._session), "request") as req, \
         mock.patch.object(path_template, "transcode")  as transcode, \
         mock.patch.object(transports.Debugger2RestInterceptor, "post_list_breakpoints") as post, \
         mock.patch.object(transports.Debugger2RestInterceptor, "pre_list_breakpoints") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = debugger.ListBreakpointsRequest.pb(debugger.ListBreakpointsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = debugger.ListBreakpointsResponse.to_json(debugger.ListBreakpointsResponse())

        request = debugger.ListBreakpointsRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = debugger.ListBreakpointsResponse()

        client.list_breakpoints(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()


def test_list_breakpoints_rest_bad_request(transport: str = 'rest', request_type=debugger.ListBreakpointsRequest):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {'debuggee_id': 'sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_breakpoints(request)


def test_list_breakpoints_rest_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = debugger.ListBreakpointsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {'debuggee_id': 'sample1'}

        # get truthy value for each flattened field
        mock_args = dict(
            debuggee_id='debuggee_id_value',
            client_version='client_version_value',
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = debugger.ListBreakpointsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value

        client.list_breakpoints(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate("%s/v2/debugger/debuggees/{debuggee_id}/breakpoints" % client.transport._host, args[1])


def test_list_breakpoints_rest_flattened_error(transport: str = 'rest'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_breakpoints(
            debugger.ListBreakpointsRequest(),
            debuggee_id='debuggee_id_value',
            client_version='client_version_value',
        )


def test_list_breakpoints_rest_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest'
    )


@pytest.mark.parametrize("request_type", [
    debugger.ListDebuggeesRequest,
    dict,
])
def test_list_debuggees_rest(request_type):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = debugger.ListDebuggeesResponse(
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = debugger.ListDebuggeesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)

        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        response = client.list_debuggees(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, debugger.ListDebuggeesResponse)


def test_list_debuggees_rest_required_fields(request_type=debugger.ListDebuggeesRequest):
    transport_class = transports.Debugger2RestTransport

    request_init = {}
    request_init["project"] = ""
    request_init["client_version"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(json_format.MessageToJson(
        pb_request,
        including_default_value_fields=False,
        use_integers_for_enums=False
    ))

    # verify fields with default values are dropped
    assert "project" not in jsonified_request
    assert "clientVersion" not in jsonified_request

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).list_debuggees._get_unset_required_fields(jsonified_request)
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "project" in jsonified_request
    assert jsonified_request["project"] == request_init["project"]
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == request_init["client_version"]

    jsonified_request["project"] = 'project_value'
    jsonified_request["clientVersion"] = 'client_version_value'

    unset_fields = transport_class(credentials=ga_credentials.AnonymousCredentials()).list_debuggees._get_unset_required_fields(jsonified_request)
    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("client_version", "include_inactive", "project", ))
    jsonified_request.update(unset_fields)

    # verify required fields with non-default values are left alone
    assert "project" in jsonified_request
    assert jsonified_request["project"] == 'project_value'
    assert "clientVersion" in jsonified_request
    assert jsonified_request["clientVersion"] == 'client_version_value'

    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest',
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = debugger.ListDebuggeesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, 'transcode') as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                'uri': 'v1/sample_method',
                'method': "get",
                'query_params': pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            pb_return_value = debugger.ListDebuggeesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(pb_return_value)

            response_value._content = json_return_value.encode('UTF-8')
            req.return_value = response_value

            response = client.list_debuggees(request)

            expected_params = [
                (
                    "project",
                    "",
                ),
                (
                    "clientVersion",
                    "",
                ),
                ('$alt', 'json;enum-encoding=int')
            ]
            actual_params = req.call_args.kwargs['params']
            assert expected_params == actual_params


def test_list_debuggees_rest_unset_required_fields():
    transport = transports.Debugger2RestTransport(credentials=ga_credentials.AnonymousCredentials)

    unset_fields = transport.list_debuggees._get_unset_required_fields({})
    assert set(unset_fields) == (set(("clientVersion", "includeInactive", "project", )) & set(("project", "clientVersion", )))


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_debuggees_rest_interceptors(null_interceptor):
    transport = transports.Debugger2RestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.Debugger2RestInterceptor(),
        )
    client = Debugger2Client(transport=transport)
    with mock.patch.object(type(client.transport._session), "request") as req, \
         mock.patch.object(path_template, "transcode")  as transcode, \
         mock.patch.object(transports.Debugger2RestInterceptor, "post_list_debuggees") as post, \
         mock.patch.object(transports.Debugger2RestInterceptor, "pre_list_debuggees") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = debugger.ListDebuggeesRequest.pb(debugger.ListDebuggeesRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = debugger.ListDebuggeesResponse.to_json(debugger.ListDebuggeesResponse())

        request = debugger.ListDebuggeesRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = debugger.ListDebuggeesResponse()

        client.list_debuggees(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()


def test_list_debuggees_rest_bad_request(transport: str = 'rest', request_type=debugger.ListDebuggeesRequest):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_debuggees(request)


def test_list_debuggees_rest_flattened():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = debugger.ListDebuggeesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {}

        # get truthy value for each flattened field
        mock_args = dict(
            project='project_value',
            client_version='client_version_value',
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        pb_return_value = debugger.ListDebuggeesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(pb_return_value)
        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value

        client.list_debuggees(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate("%s/v2/debugger/debuggees" % client.transport._host, args[1])


def test_list_debuggees_rest_flattened_error(transport: str = 'rest'):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_debuggees(
            debugger.ListDebuggeesRequest(),
            project='project_value',
            client_version='client_version_value',
        )


def test_list_debuggees_rest_error():
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest'
    )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.Debugger2GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = Debugger2Client(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.Debugger2GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = Debugger2Client(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.Debugger2GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = Debugger2Client(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = mock.Mock()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = Debugger2Client(
            client_options=options,
            credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.Debugger2GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = Debugger2Client(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.Debugger2GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = Debugger2Client(transport=transport)
    assert client.transport is transport

def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.Debugger2GrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.Debugger2GrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

@pytest.mark.parametrize("transport_class", [
    transports.Debugger2GrpcTransport,
    transports.Debugger2GrpcAsyncIOTransport,
    transports.Debugger2RestTransport,
])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, 'default') as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()

@pytest.mark.parametrize("transport_name", [
    "grpc",
    "rest",
])
def test_transport_kind(transport_name):
    transport = Debugger2Client.get_transport_class(transport_name)(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert transport.kind == transport_name

def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.Debugger2GrpcTransport,
    )

def test_debugger2_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.Debugger2Transport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json"
        )


def test_debugger2_base_transport():
    # Instantiate the base transport.
    with mock.patch('google.cloud.debugger_v2.services.debugger2.transports.Debugger2Transport.__init__') as Transport:
        Transport.return_value = None
        transport = transports.Debugger2Transport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'set_breakpoint',
        'get_breakpoint',
        'delete_breakpoint',
        'list_breakpoints',
        'list_debuggees',
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Catch all for all remaining methods and properties
    remainder = [
        'kind',
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_debugger2_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(google.auth, 'load_credentials_from_file', autospec=True) as load_creds, mock.patch('google.cloud.debugger_v2.services.debugger2.transports.Debugger2Transport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.Debugger2Transport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with("credentials.json",
            scopes=None,
            default_scopes=(
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/cloud_debugger',
),
            quota_project_id="octopus",
        )


def test_debugger2_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc, mock.patch('google.cloud.debugger_v2.services.debugger2.transports.Debugger2Transport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.Debugger2Transport()
        adc.assert_called_once()


def test_debugger2_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        Debugger2Client()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/cloud_debugger',
),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.Debugger2GrpcTransport,
        transports.Debugger2GrpcAsyncIOTransport,
    ],
)
def test_debugger2_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(                'https://www.googleapis.com/auth/cloud-platform',                'https://www.googleapis.com/auth/cloud_debugger',),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.Debugger2GrpcTransport,
        transports.Debugger2GrpcAsyncIOTransport,
        transports.Debugger2RestTransport,
    ],
)
def test_debugger2_transport_auth_gdch_credentials(transport_class):
    host = 'https://language.com'
    api_audience_tests = [None, 'https://language2.com']
    api_audience_expect = [host, 'https://language2.com']
    for t, e in zip(api_audience_tests, api_audience_expect):
        with mock.patch.object(google.auth, 'default', autospec=True) as adc:
            gdch_mock = mock.MagicMock()
            type(gdch_mock).with_gdch_audience = mock.PropertyMock(return_value=gdch_mock)
            adc.return_value = (gdch_mock, None)
            transport_class(host=host, api_audience=t)
            gdch_mock.with_gdch_audience.assert_called_once_with(
                e
            )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.Debugger2GrpcTransport, grpc_helpers),
        (transports.Debugger2GrpcAsyncIOTransport, grpc_helpers_async)
    ],
)
def test_debugger2_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(
            quota_project_id="octopus",
            scopes=["1", "2"]
        )

        create_channel.assert_called_with(
            "clouddebugger.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                'https://www.googleapis.com/auth/cloud-platform',
                'https://www.googleapis.com/auth/cloud_debugger',
),
            scopes=["1", "2"],
            default_host="clouddebugger.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("transport_class", [transports.Debugger2GrpcTransport, transports.Debugger2GrpcAsyncIOTransport])
def test_debugger2_grpc_transport_client_cert_source_for_mtls(
    transport_class
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert,
                private_key=expected_key
            )

def test_debugger2_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch("google.auth.transport.requests.AuthorizedSession.configure_mtls_channel") as mock_configure_mtls_channel:
        transports.Debugger2RestTransport (
            credentials=cred,
            client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
    "rest",
])
def test_debugger2_host_no_port(transport_name):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='clouddebugger.googleapis.com'),
         transport=transport_name,
    )
    assert client.transport._host == (
        'clouddebugger.googleapis.com:443'
        if transport_name in ['grpc', 'grpc_asyncio']
        else 'https://clouddebugger.googleapis.com'
    )

@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
    "rest",
])
def test_debugger2_host_with_port(transport_name):
    client = Debugger2Client(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='clouddebugger.googleapis.com:8000'),
        transport=transport_name,
    )
    assert client.transport._host == (
        'clouddebugger.googleapis.com:8000'
        if transport_name in ['grpc', 'grpc_asyncio']
        else 'https://clouddebugger.googleapis.com:8000'
    )

@pytest.mark.parametrize("transport_name", [
    "rest",
])
def test_debugger2_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = Debugger2Client(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = Debugger2Client(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.set_breakpoint._session
    session2 = client2.transport.set_breakpoint._session
    assert session1 != session2
    session1 = client1.transport.get_breakpoint._session
    session2 = client2.transport.get_breakpoint._session
    assert session1 != session2
    session1 = client1.transport.delete_breakpoint._session
    session2 = client2.transport.delete_breakpoint._session
    assert session1 != session2
    session1 = client1.transport.list_breakpoints._session
    session2 = client2.transport.list_breakpoints._session
    assert session1 != session2
    session1 = client1.transport.list_debuggees._session
    session2 = client2.transport.list_debuggees._session
    assert session1 != session2
def test_debugger2_grpc_transport_channel():
    channel = grpc.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.Debugger2GrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_debugger2_grpc_asyncio_transport_channel():
    channel = aio.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.Debugger2GrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class", [transports.Debugger2GrpcTransport, transports.Debugger2GrpcAsyncIOTransport])
def test_debugger2_transport_channel_mtls_with_client_cert_source(
    transport_class
):
    with mock.patch("grpc.ssl_channel_credentials", autospec=True) as grpc_ssl_channel_cred:
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, 'default') as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class", [transports.Debugger2GrpcTransport, transports.Debugger2GrpcAsyncIOTransport])
def test_debugger2_transport_channel_mtls_with_adc(
    transport_class
):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(billing_account=billing_account, )
    actual = Debugger2Client.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = Debugger2Client.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = Debugger2Client.parse_common_billing_account_path(path)
    assert expected == actual

def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(folder=folder, )
    actual = Debugger2Client.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = Debugger2Client.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = Debugger2Client.parse_common_folder_path(path)
    assert expected == actual

def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(organization=organization, )
    actual = Debugger2Client.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = Debugger2Client.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = Debugger2Client.parse_common_organization_path(path)
    assert expected == actual

def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(project=project, )
    actual = Debugger2Client.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = Debugger2Client.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = Debugger2Client.parse_common_project_path(path)
    assert expected == actual

def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(project=project, location=location, )
    actual = Debugger2Client.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = Debugger2Client.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = Debugger2Client.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(transports.Debugger2Transport, '_prep_wrapped_messages') as prep:
        client = Debugger2Client(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transports.Debugger2Transport, '_prep_wrapped_messages') as prep:
        transport_class = Debugger2Client.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

@pytest.mark.asyncio
async def test_transport_close_async():
    client = Debugger2AsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc_asyncio",
    )
    with mock.patch.object(type(getattr(client.transport, "grpc_channel")), "close") as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close():
    transports = {
        "rest": "_session",
        "grpc": "_grpc_channel",
    }

    for transport, close_name in transports.items():
        client = Debugger2Client(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport
        )
        with mock.patch.object(type(getattr(client.transport, close_name)), "close") as close:
            with client:
                close.assert_not_called()
            close.assert_called_once()

def test_client_ctx():
    transports = [
        'rest',
        'grpc',
    ]
    for transport in transports:
        client = Debugger2Client(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()

@pytest.mark.parametrize("client_class,transport_class", [
    (Debugger2Client, transports.Debugger2GrpcTransport),
    (Debugger2AsyncClient, transports.Debugger2GrpcAsyncIOTransport),
])
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )
