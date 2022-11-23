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
from google.cloud.debugger import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.debugger_v2.services.controller2.async_client import (
    Controller2AsyncClient,
)
from google.cloud.debugger_v2.services.controller2.client import Controller2Client
from google.cloud.debugger_v2.services.debugger2.async_client import (
    Debugger2AsyncClient,
)
from google.cloud.debugger_v2.services.debugger2.client import Debugger2Client
from google.cloud.debugger_v2.types.controller import (
    ListActiveBreakpointsRequest,
    ListActiveBreakpointsResponse,
    RegisterDebuggeeRequest,
    RegisterDebuggeeResponse,
    UpdateActiveBreakpointRequest,
    UpdateActiveBreakpointResponse,
)
from google.cloud.debugger_v2.types.data import (
    Breakpoint,
    Debuggee,
    FormatMessage,
    SourceLocation,
    StackFrame,
    StatusMessage,
    Variable,
)
from google.cloud.debugger_v2.types.debugger import (
    DeleteBreakpointRequest,
    GetBreakpointRequest,
    GetBreakpointResponse,
    ListBreakpointsRequest,
    ListBreakpointsResponse,
    ListDebuggeesRequest,
    ListDebuggeesResponse,
    SetBreakpointRequest,
    SetBreakpointResponse,
)

__all__ = (
    "Controller2Client",
    "Controller2AsyncClient",
    "Debugger2Client",
    "Debugger2AsyncClient",
    "ListActiveBreakpointsRequest",
    "ListActiveBreakpointsResponse",
    "RegisterDebuggeeRequest",
    "RegisterDebuggeeResponse",
    "UpdateActiveBreakpointRequest",
    "UpdateActiveBreakpointResponse",
    "Breakpoint",
    "Debuggee",
    "FormatMessage",
    "SourceLocation",
    "StackFrame",
    "StatusMessage",
    "Variable",
    "DeleteBreakpointRequest",
    "GetBreakpointRequest",
    "GetBreakpointResponse",
    "ListBreakpointsRequest",
    "ListBreakpointsResponse",
    "ListDebuggeesRequest",
    "ListDebuggeesResponse",
    "SetBreakpointRequest",
    "SetBreakpointResponse",
)
