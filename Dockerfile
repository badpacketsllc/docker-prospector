# Run prospector static analysis using docker.
# Copyright (C) 2020-2022 Bad Packets, LLC
# https://www.badpackets.net
# Licensed under a GPLv2 license
#
# To run `prospector` against code in the current directory using the image
# from Docker Hub:
# $ docker run --rm -it -v ${PWD}:/app:ro,Z badpacketsllc/prospector
#
# To build from source:
# $ docker build -t prospector .
#
# To display the command line options:
# $ docker run --rm -it prospector --help
# .. will display the command line help
#
# To run `prospector` against code in the current directory using the image
# built locally from source:
# $ docker run --rm -it -v ${PWD}:/app:ro,Z prospector

FROM docker.io/python:3.10-alpine

WORKDIR /app

RUN adduser --disabled-password prospector prospector \
    && chown -R prospector:prospector /app \
    && rm -rf ${HOME}/.cache/ ${HOME}/.local/bin/__pycache__/
USER prospector

ENV PATH /home/prospector/.local/bin:${PATH}

RUN pip3 install --no-cache-dir --compile prospector[with_everything]

ENTRYPOINT ["prospector"]
CMD []
