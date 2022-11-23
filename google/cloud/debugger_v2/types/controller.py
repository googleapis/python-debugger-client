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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.debugger_v2.types import data

__protobuf__ = proto.module(
    package="google.devtools.clouddebugger.v2",
    manifest={
        "RegisterDebuggeeRequest",
        "RegisterDebuggeeResponse",
        "ListActiveBreakpointsRequest",
        "ListActiveBreakpointsResponse",
        "UpdateActiveBreakpointRequest",
        "UpdateActiveBreakpointResponse",
    },
)


class RegisterDebuggeeRequest(proto.Message):
    r"""Request to register a debuggee.

    Attributes:
        debuggee (google.cloud.debugger_v2.types.Debuggee):
            Required. Debuggee information to register. The fields
            ``project``, ``uniquifier``, ``description`` and
            ``agent_version`` of the debuggee must be set.
    """

    debuggee: data.Debuggee = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data.Debuggee,
    )


class RegisterDebuggeeResponse(proto.Message):
    r"""Response for registering a debuggee.

    Attributes:
        debuggee (google.cloud.debugger_v2.types.Debuggee):
            Debuggee resource. The field ``id`` is guaranteed to be set
            (in addition to the echoed fields). If the field
            ``is_disabled`` is set to ``true``, the agent should disable
            itself by removing all breakpoints and detaching from the
            application. It should however continue to poll
            ``RegisterDebuggee`` until reenabled.
    """

    debuggee: data.Debuggee = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data.Debuggee,
    )


class ListActiveBreakpointsRequest(proto.Message):
    r"""Request to list active breakpoints.

    Attributes:
        debuggee_id (str):
            Required. Identifies the debuggee.
        wait_token (str):
            A token that, if specified, blocks the method call until the
            list of active breakpoints has changed, or a server-selected
            timeout has expired. The value should be set from the
            ``next_wait_token`` field in the last response. The initial
            value should be set to ``"init"``.
        success_on_timeout (bool):
            If set to ``true`` (recommended), returns
            ``google.rpc.Code.OK`` status and sets the ``wait_expired``
            response field to ``true`` when the server-selected timeout
            has expired.

            If set to ``false`` (deprecated), returns
            ``google.rpc.Code.ABORTED`` status when the server-selected
            timeout has expired.
    """

    debuggee_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    wait_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    success_on_timeout: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListActiveBreakpointsResponse(proto.Message):
    r"""Response for listing active breakpoints.

    Attributes:
        breakpoints (MutableSequence[google.cloud.debugger_v2.types.Breakpoint]):
            List of all active breakpoints. The fields ``id`` and
            ``location`` are guaranteed to be set on each breakpoint.
        next_wait_token (str):
            A token that can be used in the next method
            call to block until the list of breakpoints
            changes.
        wait_expired (bool):
            If set to ``true``, indicates that there is no change to the
            list of active breakpoints and the server-selected timeout
            has expired. The ``breakpoints`` field would be empty and
            should be ignored.
    """

    breakpoints: MutableSequence[data.Breakpoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=data.Breakpoint,
    )
    next_wait_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    wait_expired: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class UpdateActiveBreakpointRequest(proto.Message):
    r"""Request to update an active breakpoint.

    Attributes:
        debuggee_id (str):
            Required. Identifies the debuggee being
            debugged.
        breakpoint_ (google.cloud.debugger_v2.types.Breakpoint):
            Required. Updated breakpoint information. The field ``id``
            must be set. The agent must echo all Breakpoint
            specification fields in the update.
    """

    debuggee_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    breakpoint_: data.Breakpoint = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data.Breakpoint,
    )


class UpdateActiveBreakpointResponse(proto.Message):
    r"""Response for updating an active breakpoint.
    The message is defined to allow future extensions.

    """


__all__ = tuple(sorted(__protobuf__.manifest))
