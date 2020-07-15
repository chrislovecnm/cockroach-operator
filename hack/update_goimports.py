#!/usr/bin/env python

# Copyright 2020 Coachroach Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Verifies that all source files contain the necessary copyright boilerplate
# snippet.

import os
from os import path
import subprocess
import sys

from lib.kubernetes import devtools

gopath=os.environ['GOPATH']

package_name='k8s.io/kops'

packages = devtools.read_packages_file(package_name)

paths = []

for package in packages:
  if package == package_name:
    continue
  paths.append(package)

print("packages %s" % paths)

subprocess.call(['go', 'run', 'golang.org/x/tools/cmd/goimports', '-w'] + paths, cwd=path.join(gopath, 'src'))
