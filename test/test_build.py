"""
prospector container build test suite
Copyright (C) 2020-2022 Bad Packets, LLC
https://www.badpackets.net

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
