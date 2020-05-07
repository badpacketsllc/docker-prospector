# prospector
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/badpacketsllc/docker-prospector/graphs/commit-activity)
[![Build status](https://img.shields.io/travis/com/badpacketsllc/docker-prospector.svg?style=flat)](https://travis-ci.com/badpacketsllc/docker-prospector)
[![Docker image download](https://img.shields.io/docker/pulls/badpacketsllc/prospector)](https://hub.docker.com/r/badpacketsllc/prospector)
[![License](https://img.shields.io/github/license/badpacketsllc/docker-prospector?style=flat)](https://github.com/badpacketsllc/docker-prospector/blob/master/LICENSE)
[![Follow us on twitter](https://img.shields.io/twitter/follow/bad_packets.svg?style=social)](https://twitter.com/bad_packets/)

Prospector docker container image

Building
--------

Build the container locally by running `$ docker build -t prospector .`

Usage
-----

To run `prospector` against code in the current directory using the image
from Docker Hub:

`$ docker run --rm -it  -v ${PWD}:/data:ro,Z badpacketsllc/prospector`

To run `prospector` against code in the current directory using the image
built locally from source:

`$ docker run --rm -it  -v ${PWD}:/data:ro,Z prospector`

Running tests
-------------

In order to keep code quality high, all merges must pass tests and static
analysis. Currently, the test suite is designed to run locally like so
(assuming you have Python 3.6 or higher available).

```shell script
$ pip3 install --user pipenv
$ pipenv install --dev
$ pipenv run yamllint .
$ pipenv run prospector
$ pipenv run pytest
```

Travis runs the test suite whenever you push a commit to make sure everything
is sane, but running the test suite locally before you push saves a lot of
time!

Contributing
------------

Contributions are encouraged! Learn how to contribute by reading
[CONTRIBUTING.md](https://github.com/badpacketsllc/docker-prospector/blob/master/CONTRIBUTING.md).
Please be nice and follow our
[Code of Conduct](https://github.com/badpacketsllc/docker-prospector/blob/master/CODE_OF_CONDUCT.md).

License
-------

GPLv2

Author Information
------------------

[Mathew Woodyard](https://www.matwoodyard.com)

[Bad Packets LLC](https://badpackets.net)
