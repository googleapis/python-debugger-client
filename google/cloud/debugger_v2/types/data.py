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

from google.cloud.source_context_v1.types import (
    source_context as source_context_pb2,
)  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.protobuf import wrappers_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devtools.clouddebugger.v2",
    manifest={
        "FormatMessage",
        "StatusMessage",
        "SourceLocation",
        "Variable",
        "StackFrame",
        "Breakpoint",
        "Debuggee",
    },
)


class FormatMessage(proto.Message):
    r"""Represents a message with parameters.

    Attributes:
        format_ (str):
            Format template for the message. The ``format`` uses
            placeholders ``$0``, ``$1``, etc. to reference parameters.
            ``$$`` can be used to denote the ``$`` character.

            Examples:

            -  ``Failed to load '$0' which helps debug $1 the first time it is loaded. Again, $0 is very important.``
            -  ``Please pay $$10 to use $0 instead of $1.``
        parameters (MutableSequence[str]):
            Optional parameters to be embedded into the
            message.
    """

    format_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class StatusMessage(proto.Message):
    r"""Represents a contextual status message. The message can indicate an
    error or informational status, and refer to specific parts of the
    containing object. For example, the ``Breakpoint.status`` field can
    indicate an error referring to the ``BREAKPOINT_SOURCE_LOCATION``
    with the message ``Location not found``.

    Attributes:
        is_error (bool):
            Distinguishes errors from informational
            messages.
        refers_to (google.cloud.debugger_v2.types.StatusMessage.Reference):
            Reference to which the message applies.
        description (google.cloud.debugger_v2.types.FormatMessage):
            Status message text.
    """

    class Reference(proto.Enum):
        r"""Enumerates references to which the message applies."""
        UNSPECIFIED = 0
        BREAKPOINT_SOURCE_LOCATION = 3
        BREAKPOINT_CONDITION = 4
        BREAKPOINT_EXPRESSION = 7
        BREAKPOINT_AGE = 8
        VARIABLE_NAME = 5
        VARIABLE_VALUE = 6

    is_error: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    refers_to: Reference = proto.Field(
        proto.ENUM,
        number=2,
        enum=Reference,
    )
    description: "FormatMessage" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="FormatMessage",
    )


class SourceLocation(proto.Message):
    r"""Represents a location in the source code.

    Attributes:
        path (str):
            Path to the source file within the source
            context of the target binary.
        line (int):
            Line inside the file. The first line in the file has the
            value ``1``.
        column (int):
            Column within a line. The first column in a line as the
            value ``1``. Agents that do not support setting breakpoints
            on specific columns ignore this field.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    line: int = proto.Field(
        proto.INT32,
        number=2,
    )
    column: int = proto.Field(
        proto.INT32,
        number=3,
    )


class Variable(proto.Message):
    r"""Represents a variable or an argument possibly of a compound object
    type. Note how the following variables are represented:

    1) A simple variable:

       int x = 5

       { name: "x", value: "5", type: "int" } // Captured variable

    2) A compound object:

       struct T { int m1; int m2; }; T x = { 3, 7 };

       { // Captured variable name: "x", type: "T", members { name:
       "m1", value: "3", type: "int" }, members { name: "m2", value:
       "7", type: "int" } }

    3) A pointer where the pointee was captured:

       T x = { 3, 7 }; T\* p = &x;

       { // Captured variable name: "p", type: "T*", value:
       "0x00500500", members { name: "m1", value: "3", type: "int" },
       members { name: "m2", value: "7", type: "int" } }

    4) A pointer where the pointee was not captured:

       T\* p = new T;

       { // Captured variable name: "p", type: "T*", value: "0x00400400"
       status { is_error: true, description { format: "unavailable" } }
       }

    The status should describe the reason for the missing value, such as
    ``<optimized out>``, ``<inaccessible>``,
    ``<pointers limit reached>``.

    Note that a null pointer should not have members.

    5) An unnamed value:

       int\* p = new int(7);

       { // Captured variable name: "p", value: "0x00500500", type:
       "int*", members { value: "7", type: "int" } }

    6) An unnamed pointer where the pointee was not captured:

       int\* p = new int(7); int*\* pp = &p;

       { // Captured variable name: "pp", value: "0x00500500", type:
       "int**", members { value: "0x00400400", type: "int*" status {
       is_error: true, description: { format: "unavailable" } } } } }

    To optimize computation, memory and network traffic, variables that
    repeat in the output multiple times can be stored once in a shared
    variable table and be referenced using the ``var_table_index``
    field. The variables stored in the shared table are nameless and are
    essentially a partition of the complete variable. To reconstruct the
    complete variable, merge the referencing variable with the
    referenced variable.

    When using the shared variable table, the following variables:

    ::

        T x = { 3, 7 };
        T* p = &x;
        T& r = x;

        { name: "x", var_table_index: 3, type: "T" }  // Captured variables
        { name: "p", value "0x00500500", type="T*", var_table_index: 3 }
        { name: "r", type="T&", var_table_index: 3 }

        {  // Shared variable table entry #3:
            members { name: "m1", value: "3", type: "int" },
            members { name: "m2", value: "7", type: "int" }
        }

    Note that the pointer address is stored with the referencing
    variable and not with the referenced variable. This allows the
    referenced variable to be shared between pointers and references.

    The type field is optional. The debugger agent may or may not
    support it.

    Attributes:
        name (str):
            Name of the variable, if any.
        value (str):
            Simple value of the variable.
        type_ (str):
            Variable type (e.g. ``MyClass``). If the variable is split
            with ``var_table_index``, ``type`` goes next to ``value``.
            The interpretation of a type is agent specific. It is
            recommended to include the dynamic type rather than a static
            type of an object.
        members (MutableSequence[google.cloud.debugger_v2.types.Variable]):
            Members contained or pointed to by the
            variable.
        var_table_index (google.protobuf.wrappers_pb2.Int32Value):
            Reference to a variable in the shared variable table. More
            than one variable can reference the same variable in the
            table. The ``var_table_index`` field is an index into
            ``variable_table`` in Breakpoint.
        status (google.cloud.debugger_v2.types.StatusMessage):
            Status associated with the variable. This field will usually
            stay unset. A status of a single variable only applies to
            that variable or expression. The rest of breakpoint data
            still remains valid. Variables might be reported in error
            state even when breakpoint is not in final state.

            The message may refer to variable name with ``refers_to``
            set to ``VARIABLE_NAME``. Alternatively ``refers_to`` will
            be set to ``VARIABLE_VALUE``. In either case variable value
            and members will be unset.

            Example of error message applied to name:
            ``Invalid expression syntax``.

            Example of information message applied to value:
            ``Not captured``.

            Examples of error message applied to value:

            -  ``Malformed string``,
            -  ``Field f not found in class C``
            -  ``Null pointer dereference``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=6,
    )
    members: MutableSequence["Variable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Variable",
    )
    var_table_index: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int32Value,
    )
    status: "StatusMessage" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="StatusMessage",
    )


class StackFrame(proto.Message):
    r"""Represents a stack frame context.

    Attributes:
        function (str):
            Demangled function name at the call site.
        location (google.cloud.debugger_v2.types.SourceLocation):
            Source location of the call site.
        arguments (MutableSequence[google.cloud.debugger_v2.types.Variable]):
            Set of arguments passed to this function.
            Note that this might not be populated for all
            stack frames.
        locals_ (MutableSequence[google.cloud.debugger_v2.types.Variable]):
            Set of local variables at the stack frame
            location. Note that this might not be populated
            for all stack frames.
    """

    function: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: "SourceLocation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SourceLocation",
    )
    arguments: MutableSequence["Variable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Variable",
    )
    locals_: MutableSequence["Variable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Variable",
    )


class Breakpoint(proto.Message):
    r"""Represents the breakpoint specification, status and results.

    Attributes:
        id (str):
            Breakpoint identifier, unique in the scope of
            the debuggee.
        action (google.cloud.debugger_v2.types.Breakpoint.Action):
            Action that the agent should perform when the
            code at the breakpoint location is hit.
        location (google.cloud.debugger_v2.types.SourceLocation):
            Breakpoint source location.
        condition (str):
            Condition that triggers the breakpoint.
            The condition is a compound boolean expression
            composed using expressions in a programming
            language at the source location.
        expressions (MutableSequence[str]):
            List of read-only expressions to evaluate at the breakpoint
            location. The expressions are composed using expressions in
            the programming language at the source location. If the
            breakpoint action is ``LOG``, the evaluated expressions are
            included in log statements.
        log_message_format (str):
            Only relevant when action is ``LOG``. Defines the message to
            log when the breakpoint hits. The message may include
            parameter placeholders ``$0``, ``$1``, etc. These
            placeholders are replaced with the evaluated value of the
            appropriate expression. Expressions not referenced in
            ``log_message_format`` are not logged.

            Example: ``Message received, id = $0, count = $1`` with
            ``expressions`` = ``[ message.id, message.count ]``.
        log_level (google.cloud.debugger_v2.types.Breakpoint.LogLevel):
            Indicates the severity of the log. Only relevant when action
            is ``LOG``.
        is_final_state (bool):
            When true, indicates that this is a final
            result and the breakpoint state will not change
            from here on.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time this breakpoint was created by the
            server in seconds resolution.
        final_time (google.protobuf.timestamp_pb2.Timestamp):
            Time this breakpoint was finalized as seen by
            the server in seconds resolution.
        user_email (str):
            E-mail address of the user that created this
            breakpoint
        status (google.cloud.debugger_v2.types.StatusMessage):
            Breakpoint status.

            The status includes an error flag and a human readable
            message. This field is usually unset. The message can be
            either informational or an error message. Regardless,
            clients should always display the text message back to the
            user.

            Error status indicates complete failure of the breakpoint.

            Example (non-final state): ``Still loading symbols...``

            Examples (final state):

            -  ``Invalid line number`` referring to location
            -  ``Field f not found in class C`` referring to condition
        stack_frames (MutableSequence[google.cloud.debugger_v2.types.StackFrame]):
            The stack at breakpoint time, where stack_frames[0]
            represents the most recently entered function.
        evaluated_expressions (MutableSequence[google.cloud.debugger_v2.types.Variable]):
            Values of evaluated expressions at breakpoint time. The
            evaluated expressions appear in exactly the same order they
            are listed in the ``expressions`` field. The ``name`` field
            holds the original expression text, the ``value`` or
            ``members`` field holds the result of the evaluated
            expression. If the expression cannot be evaluated, the
            ``status`` inside the ``Variable`` will indicate an error
            and contain the error text.
        variable_table (MutableSequence[google.cloud.debugger_v2.types.Variable]):
            The ``variable_table`` exists to aid with computation,
            memory and network traffic optimization. It enables storing
            a variable once and reference it from multiple variables,
            including variables stored in the ``variable_table`` itself.
            For example, the same ``this`` object, which may appear at
            many levels of the stack, can have all of its data stored
            once in this table. The stack frame variables then would
            hold only a reference to it.

            The variable ``var_table_index`` field is an index into this
            repeated field. The stored objects are nameless and get
            their name from the referencing variable. The effective
            variable is a merge of the referencing variable and the
            referenced variable.
        labels (MutableMapping[str, str]):
            A set of custom breakpoint properties,
            populated by the agent, to be displayed to the
            user.
    """

    class Action(proto.Enum):
        r"""Actions that can be taken when a breakpoint hits.
        Agents should reject breakpoints with unsupported or unknown
        action values.
        """
        CAPTURE = 0
        LOG = 1

    class LogLevel(proto.Enum):
        r"""Log severity levels."""
        INFO = 0
        WARNING = 1
        ERROR = 2

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action: Action = proto.Field(
        proto.ENUM,
        number=13,
        enum=Action,
    )
    location: "SourceLocation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SourceLocation",
    )
    condition: str = proto.Field(
        proto.STRING,
        number=3,
    )
    expressions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    log_message_format: str = proto.Field(
        proto.STRING,
        number=14,
    )
    log_level: LogLevel = proto.Field(
        proto.ENUM,
        number=15,
        enum=LogLevel,
    )
    is_final_state: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    final_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    user_email: str = proto.Field(
        proto.STRING,
        number=16,
    )
    status: "StatusMessage" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="StatusMessage",
    )
    stack_frames: MutableSequence["StackFrame"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="StackFrame",
    )
    evaluated_expressions: MutableSequence["Variable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="Variable",
    )
    variable_table: MutableSequence["Variable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Variable",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=17,
    )


class Debuggee(proto.Message):
    r"""Represents the debugged application. The application may
    include one or more replicated processes executing the same
    code. Each of these processes is attached with a debugger agent,
    carrying out the debugging commands. Agents attached to the same
    debuggee identify themselves as such by using exactly the same
    Debuggee message value when registering.

    Attributes:
        id (str):
            Unique identifier for the debuggee generated
            by the controller service.
        project (str):
            Project the debuggee is associated with.
            Use project number or id when registering a
            Google Cloud Platform project.
        uniquifier (str):
            Uniquifier to further distinguish the
            application. It is possible that different
            applications might have identical values in the
            debuggee message, thus, incorrectly identified
            as a single application by the Controller
            service. This field adds salt to further
            distinguish the application. Agents should
            consider seeding this field with value that
            identifies the code, binary, configuration and
            environment.
        description (str):
            Human readable description of the debuggee.
            Including a human-readable project name,
            environment name and version information is
            recommended.
        is_inactive (bool):
            If set to ``true``, indicates that Controller service does
            not detect any activity from the debuggee agents and the
            application is possibly stopped.
        agent_version (str):
            Version ID of the agent. Schema:
            ``domain/language-platform/vmajor.minor`` (for example
            ``google.com/java-gcp/v1.1``).
        is_disabled (bool):
            If set to ``true``, indicates that the agent should disable
            itself and detach from the debuggee.
        status (google.cloud.debugger_v2.types.StatusMessage):
            Human readable message to be displayed to the
            user about this debuggee. Absence of this field
            indicates no status. The message can be either
            informational or an error status.
        source_contexts (MutableSequence[google.cloud.source_context_v1.types.source_context_pb2.SourceContext]):
            References to the locations and revisions of
            the source code used in the deployed
            application.
        ext_source_contexts (MutableSequence[google.cloud.source_context_v1.types.source_context_pb2.ExtendedSourceContext]):
            References to the locations and revisions of
            the source code used in the deployed
            application.
        labels (MutableMapping[str, str]):
            A set of custom debuggee properties,
            populated by the agent, to be displayed to the
            user.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uniquifier: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    is_inactive: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    agent_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    is_disabled: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    status: "StatusMessage" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="StatusMessage",
    )
    source_contexts: MutableSequence[
        source_context_pb2.SourceContext
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=source_context_pb2.SourceContext,
    )
    ext_source_contexts: MutableSequence[
        source_context_pb2.ExtendedSourceContext
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message=source_context_pb2.ExtendedSourceContext,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
