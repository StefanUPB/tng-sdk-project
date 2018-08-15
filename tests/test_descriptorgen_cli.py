#!/usr/bin/python3

#  Copyright (c) 2015 SONATA-NFV, 5GTANGO, UBIWHERE, Paderborn University
# ALL RIGHTS RESERVED.
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
# Neither the name of the SONATA-NFV, 5GTANGO, UBIWHERE, Paderborn University
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has been performed in the framework of the SONATA project,
# funded by the European Commission under Grant number 671517 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.sonata-nfv.eu).
#
# This work has also been performed in the framework of the 5GTANGO project,
# funded by the European Commission under Grant number 761493 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.5gtango.eu).

import pytest
import os
import shutil
import yaml
import tngsdk.descriptorgen.descriptorgen as cli


class TestDescriptorgenCLI:
    # generate descriptors with custom author, vendor, name, description
    def test_generate_custom_descriptors(self):
        args = cli.parse_args([
            '--author', 'test.author',
            '--vendor', 'test.vendor',
            '--name', 'test.service',
            '--description', 'test.description',
            '-o', 'test-descriptorgen'
        ])
        cli.generate(args)

        # FIXME: check yaml values of both Tango and OSM descriptors
        assert True

        shutil.rmtree('test-descriptorgen')

    # TODO: generate multiple diff. #VNFs, check resulting file names
    # TODO: generate only tango/osm descriptors; check file names
