# Copyright 2021 Google LLC
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

import synthtool as s
import synthtool.gcp as gcp
from synthtool.languages import python

# ----------------------------------------------------------------------------
# Copy the generated client from the owl-bot staging directory
# ----------------------------------------------------------------------------

default_version = "v2"

for library in s.get_staging_dirs(default_version):
    # Work around gapic generator bug https://github.com/googleapis/gapic-generator-python/issues/902
    s.replace(
        [
            library / f"google/cloud/debugger_{library.name}/types/data.py",
            library / f"google/cloud/debugger_{library.name}/types/debugger.py",
        ],
        r""".
    Attributes:""",
        r""".\n
    Attributes:""",
    )

    # Replace `google.devtools.source.v1` with `google.cloud.source_context_v1.types`
    s.replace(
        [
            library / f"google/cloud/debugger_{library.name}/types/data.py",
            library / f"tests/unit/gapic/debugger_{library.name}/test_controller2.py",
        ],
        "from google.devtools.source.v1 import source_context_pb2",
        "from google.cloud.source_context_v1.types import source_context as source_context_pb2"
    )

    # Replace `google.devtools.source.v1` with `google.cloud.source_context_v1.types`
    s.replace(library / f"google/cloud/debugger_{library.name}/types/data.py",
        "google.devtools.source.v1.source_context_pb2",
        "google.cloud.source_context_v1.types.source_context_pb2"
    )

    s.move(library, excludes=["setup.py", "README.rst", "docs/index.rst"])

s.remove_staging_dirs()

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------

templated_files = gcp.CommonTemplates().py_library(cov_level=99, microgenerator=True)
python.py_samples(skip_readmes=True)
s.move(templated_files, excludes=[".coveragerc"]) # the microgenerator has a good coveragerc file
# Remove the replacements below once https://github.com/googleapis/synthtool/pull/1188 is merged

# Update googleapis/repo-automation-bots repo to main in .kokoro/*.sh files
s.replace(".kokoro/*.sh", "repo-automation-bots/tree/master", "repo-automation-bots/tree/main")

# Customize CONTRIBUTING.rst to replace master with main
s.replace(
    "CONTRIBUTING.rst",
    "fetch and merge changes from upstream into master",
    "fetch and merge changes from upstream into main",
)

s.replace(
    "CONTRIBUTING.rst",
    "git merge upstream/master",
    "git merge upstream/main",
)

s.replace(
    "CONTRIBUTING.rst",
    """export GOOGLE_CLOUD_TESTING_BRANCH=\"master\"""",
    """export GOOGLE_CLOUD_TESTING_BRANCH=\"main\"""",
)

s.replace(
    "CONTRIBUTING.rst",
    "remote \(``master``\)",
    "remote (``main``)",
)

s.replace(
    "CONTRIBUTING.rst",
    "blob/master/CONTRIBUTING.rst",
    "blob/main/CONTRIBUTING.rst",
)

s.replace(
    "CONTRIBUTING.rst",
    "blob/master/noxfile.py",
    "blob/main/noxfile.py",
)

s.replace(
    "docs/conf.py",
    "master_doc",
    "root_doc",
)

s.replace(
    "docs/conf.py",
    "# The master toctree document.",
    "# The root toctree document.",
)

# ----------------------------------------------------------------------------
# Run blacken session
# ----------------------------------------------------------------------------

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
