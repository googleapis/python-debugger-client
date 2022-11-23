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


from .services.controller2 import Controller2AsyncClient, Controller2Client
from .services.debugger2 import Debugger2AsyncClient, Debugger2Client
from .types.controller import (
    ListActiveBreakpointsRequest,
    ListActiveBreakpointsResponse,
    RegisterDebuggeeRequest,
    RegisterDebuggeeResponse,
    UpdateActiveBreakpointRequest,
    UpdateActiveBreakpointResponse,
)
from .types.data import (
    Breakpoint,
    Debuggee,
    FormatMessage,
    SourceLocation,
    StackFrame,
    StatusMessage,
    Variable,
)
from .types.debugger import (
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
    "Controller2AsyncClient",
    "Debugger2AsyncClient",
    "Breakpoint",
    "Controller2Client",
    "Debuggee",
    "Debugger2Client",
    "DeleteBreakpointRequest",
    "FormatMessage",
    "GetBreakpointRequest",
    "GetBreakpointResponse",
    "ListActiveBreakpointsRequest",
    "ListActiveBreakpointsResponse",
    "ListBreakpointsRequest",
    "ListBreakpointsResponse",
    "ListDebuggeesRequest",
    "ListDebuggeesResponse",
    "RegisterDebuggeeRequest",
    "RegisterDebuggeeResponse",
    "SetBreakpointRequest",
    "SetBreakpointResponse",
    "SourceLocation",
    "StackFrame",
    "StatusMessage",
    "UpdateActiveBreakpointRequest",
    "UpdateActiveBreakpointResponse",
    "Variable",
)
