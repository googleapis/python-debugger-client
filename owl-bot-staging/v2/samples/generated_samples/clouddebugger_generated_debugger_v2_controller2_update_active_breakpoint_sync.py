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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateActiveBreakpoint
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-debugger-client


# [START clouddebugger_generated_debugger_v2_Controller2_UpdateActiveBreakpoint_sync]
from google.cloud import debugger_v2


def sample_update_active_breakpoint():
    # Create a client
    client = debugger_v2.Controller2Client()

    # Initialize request argument(s)
    request = debugger_v2.UpdateActiveBreakpointRequest(
        debuggee_id="debuggee_id_value",
    )

    # Make the request
    response = client.update_active_breakpoint(request=request)

    # Handle response
    print(response)

# [END clouddebugger_generated_debugger_v2_Controller2_UpdateActiveBreakpoint_sync]
