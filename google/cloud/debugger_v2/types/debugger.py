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
        "SetBreakpointRequest",
        "SetBreakpointResponse",
        "GetBreakpointRequest",
        "GetBreakpointResponse",
        "DeleteBreakpointRequest",
        "ListBreakpointsRequest",
        "ListBreakpointsResponse",
        "ListDebuggeesRequest",
        "ListDebuggeesResponse",
    },
)


class SetBreakpointRequest(proto.Message):
    r"""Request to set a breakpoint

    Attributes:
        debuggee_id (str):
            Required. ID of the debuggee where the
            breakpoint is to be set.
        breakpoint_ (google.cloud.debugger_v2.types.Breakpoint):
            Required. Breakpoint specification to set. The field
            ``location`` of the breakpoint must be set.
        client_version (str):
            Required. The client version making the call. Schema:
            ``domain/type/version`` (e.g., ``google.com/intellij/v1``).
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
    client_version: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SetBreakpointResponse(proto.Message):
    r"""Response for setting a breakpoint.

    Attributes:
        breakpoint_ (google.cloud.debugger_v2.types.Breakpoint):
            Breakpoint resource. The field ``id`` is guaranteed to be
            set (in addition to the echoed fileds).
    """

    breakpoint_: data.Breakpoint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data.Breakpoint,
    )


class GetBreakpointRequest(proto.Message):
    r"""Request to get breakpoint information.

    Attributes:
        debuggee_id (str):
            Required. ID of the debuggee whose breakpoint
            to get.
        breakpoint_id (str):
            Required. ID of the breakpoint to get.
        client_version (str):
            Required. The client version making the call. Schema:
            ``domain/type/version`` (e.g., ``google.com/intellij/v1``).
    """

    debuggee_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    breakpoint_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_version: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetBreakpointResponse(proto.Message):
    r"""Response for getting breakpoint information.

    Attributes:
        breakpoint_ (google.cloud.debugger_v2.types.Breakpoint):
            Complete breakpoint state. The fields ``id`` and
            ``location`` are guaranteed to be set.
    """

    breakpoint_: data.Breakpoint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data.Breakpoint,
    )


class DeleteBreakpointRequest(proto.Message):
    r"""Request to delete a breakpoint.

    Attributes:
        debuggee_id (str):
            Required. ID of the debuggee whose breakpoint
            to delete.
        breakpoint_id (str):
            Required. ID of the breakpoint to delete.
        client_version (str):
            Required. The client version making the call. Schema:
            ``domain/type/version`` (e.g., ``google.com/intellij/v1``).
    """

    debuggee_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    breakpoint_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListBreakpointsRequest(proto.Message):
    r"""Request to list breakpoints.

    Attributes:
        debuggee_id (str):
            Required. ID of the debuggee whose
            breakpoints to list.
        include_all_users (bool):
            When set to ``true``, the response includes the list of
            breakpoints set by any user. Otherwise, it includes only
            breakpoints set by the caller.
        include_inactive (bool):
            When set to ``true``, the response includes active and
            inactive breakpoints. Otherwise, it includes only active
            breakpoints.
        action (google.cloud.debugger_v2.types.ListBreakpointsRequest.BreakpointActionValue):
            When set, the response includes only
            breakpoints with the specified action.
        strip_results (bool):
            This field is deprecated. The following fields are always
            stripped out of the result: ``stack_frames``,
            ``evaluated_expressions`` and ``variable_table``.
        wait_token (str):
            A wait token that, if specified, blocks the call until the
            breakpoints list has changed, or a server selected timeout
            has expired. The value should be set from the last response.
            The error code ``google.rpc.Code.ABORTED`` (RPC) is returned
            on wait timeout, which should be called again with the same
            ``wait_token``.
        client_version (str):
            Required. The client version making the call. Schema:
            ``domain/type/version`` (e.g., ``google.com/intellij/v1``).
    """

    class BreakpointActionValue(proto.Message):
        r"""Wrapper message for ``Breakpoint.Action``. Defines a filter on the
        action field of breakpoints.

        Attributes:
            value (google.cloud.debugger_v2.types.Breakpoint.Action):
                Only breakpoints with the specified action
                will pass the filter.
        """

        value: data.Breakpoint.Action = proto.Field(
            proto.ENUM,
            number=1,
            enum=data.Breakpoint.Action,
        )

    debuggee_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    include_all_users: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    include_inactive: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    action: BreakpointActionValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=BreakpointActionValue,
    )
    strip_results: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    wait_token: str = proto.Field(
        proto.STRING,
        number=6,
    )
    client_version: str = proto.Field(
        proto.STRING,
        number=8,
    )


class ListBreakpointsResponse(proto.Message):
    r"""Response for listing breakpoints.

    Attributes:
        breakpoints (MutableSequence[google.cloud.debugger_v2.types.Breakpoint]):
            List of breakpoints matching the request. The fields ``id``
            and ``location`` are guaranteed to be set on each
            breakpoint. The fields: ``stack_frames``,
            ``evaluated_expressions`` and ``variable_table`` are cleared
            on each breakpoint regardless of its status.
        next_wait_token (str):
            A wait token that can be used in the next call to ``list``
            (REST) or ``ListBreakpoints`` (RPC) to block until the list
            of breakpoints has changes.
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


class ListDebuggeesRequest(proto.Message):
    r"""Request to list debuggees.

    Attributes:
        project (str):
            Required. Project number of a Google Cloud
            project whose debuggees to list.
        include_inactive (bool):
            When set to ``true``, the result includes all debuggees.
            Otherwise, the result includes only debuggees that are
            active.
        client_version (str):
            Required. The client version making the call. Schema:
            ``domain/type/version`` (e.g., ``google.com/intellij/v1``).
    """

    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    include_inactive: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    client_version: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDebuggeesResponse(proto.Message):
    r"""Response for listing debuggees.

    Attributes:
        debuggees (MutableSequence[google.cloud.debugger_v2.types.Debuggee]):
            List of debuggees accessible to the calling user. The fields
            ``debuggee.id`` and ``description`` are guaranteed to be
            set. The ``description`` field is a human readable field
            provided by agents and can be displayed to users.
    """

    debuggees: MutableSequence[data.Debuggee] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=data.Debuggee,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
