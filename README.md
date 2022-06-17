# docker-prospector
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/badpacketsllc/docker-prospector/graphs/commit-activity)
![Build Status](https://github.com/badpacketsllc/docker-prospector/workflows/ci/badge.svg)
[![Docker image download](https://img.shields.io/docker/pulls/badpacketsllc/prospector)](https://hub.docker.com/r/badpacketsllc/prospector)
[![License](https://img.shields.io/github/license/badpacketsllc/docker-prospector?style=flat)](https://github.com/badpacketsllc/docker-prospector/blob/master/LICENSE)
[![Follow us on twitter](https://img.shields.io/twitter/follow/bad_packets.svg?style=social)](https://twitter.com/bad_packets/)

Prospector container image intended for use in both CI pipelines and
local environments.

Building
--------

Build the container locally by running `$ docker build -t prospector .`

Usage
-----

### Local

To run `prospector` against code in the current directory using the image
from Docker Hub:

`$ docker run --rm -it -v ${PWD}:/app:ro,Z badpacketsllc/prospector`

To run `prospector` against code in the current directory using the image
built locally from source:

`$ docker run --rm -it -v ${PWD}:/app:ro,Z prospector`

### In GitLab CI flows

To run this image in your GitLab CI pipeline, you can add a `.gitlab-ci.yml`
file to your repository that looks like:

```yaml
stages:
  - lint

prospector:
  stage: lint
  image:
    name: badpacketsllc/prospector
    entrypoint: [""]
  script: prospector

```

Running tests
-------------

In order to keep code quality high, all merges must pass tests and static
analysis.

### Locally, with Docker and Python 3.6 or higher

```shell script
$ pip3 install -r requirements-dev.txt
$ yamllint .
$ prospector ./test/test_build.py
$ pytest
```

### Locally, using [`act`](https://github.com/nektos/act)

`act` is a library that allows you to test GitHub Actions locally. To get
started, first [install `act`](https://github.com/nektos/act#installation).
Once you have `act` installed, you may run `act` to simulate the merge workflow
and use other
[helpful commands](https://github.com/nektos/act#example-commands) to perform
any other task defined in te GitHub Actions workflow.


GitHub actions run the test suite whenever you push a commit to make sure
everything looks sane, but running the test suite locally before you push
saves a lot of time!

Contributing
------------

Contributions are encouraged! Learn how to contribute by reading
[CONTRIBUTING.md](https://github.com/badpacketsllc/docker-prospector/blob/master/CONTRIBUTING.md).
Please be nice and follow our
[Code of Conduct](https://github.com/badpacketsllc/docker-prospector/blob/master/CODE_OF_CONDUCT.md).

License
-------

Apache License 2.0

Author Information
------------------

[Mathew Woodyard](https://www.matwoodyard.com)
