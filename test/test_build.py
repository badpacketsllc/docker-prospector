"""
prospector container build test suite
Copyright (C) 2022 Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import subprocess
import os
import pytest
import testinfra


@pytest.fixture(scope='session')
def host(request):  # pylint:disable=unused-argument
    subprocess.check_call(['docker', 'build',
                           '-t', 'badpacketsllc/prospector', '.'])

    docker_base_command = ['docker', 'run', '-d']
    pwd = os.getcwd()
    volume_mount_option = ['-v', f'{pwd}:/app:ro,Z']

    docker_id = subprocess.check_output(docker_base_command +
                                        volume_mount_option +
                                        ['badpacketsllc/prospector']
                                        ).decode().strip()

    yield testinfra.get_host(f'docker://{docker_id}')
    subprocess.check_call(['docker', 'rm', '-f', docker_id])


def test_good_code(host):
    """
    Tests the stdout text from running `prospector`. exit code is not checked
    because `prospector` can return a non-zero code when executing from a
    container, even when `prospector` finds no problems.
    """
    cmd = host.run('prospector ./test/good_code.py')
    assert 'Messages Found: 0' in cmd.stdout


def test_bad_code(host):
    """
    Tests for failure after running `prospector`. We assert that the exit code
    is nonzero rather than equal to 1 because `prospector` failures can return
    any non-zero code when executing from a container, even though `prospector`
    should only ever return 1 when failing in a normal scenario.
    """
    exit_code = host.run('prospector ./test/bad_code.py').rc
    assert exit_code != 0
