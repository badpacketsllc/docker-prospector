"""
    prospector docker build test suite
    Copyright (C) 2020 Bad Packets, LLC
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


import pytest
import subprocess
import testinfra


@pytest.fixture(scope='session')
def host(request):  # noqa: unused-argument
    subprocess.check_call(['docker', 'build', '-t', 'prospector', '.'])
    docker_id = subprocess.check_output(
        ['docker', 'run', '-d', 'prospector']).decode().strip()
    yield testinfra.get_host(f'docker://{docker_id}')
    subprocess.check_call(['docker', 'rm', '-f', docker_id])


def test_passing_code(host):
    assert host.run('prospector test/good_code.py').rc == 1


def test_failing_code(host):
    assert host.run('prospector test/bad_code.py').rc != 1
