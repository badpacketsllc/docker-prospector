# Run prospector static analysis using docker.
#
# To build:
# $ docker build -t prospector .
#
# To run:
# To display the command line options:
# $ docker run --rm -it prospector --help
# .. will display the command line help
#
# To run `prospector` against code in the current directory using the image
# from Docker Hub:
# $ docker run --rm -it  -v ${PWD}:/data:ro,Z badpacketsllc/prospector
#
# To run `prospector` against code in the current directory using the image
# built locally from source
# $ docker run --rm -it  -v ${PWD}:/data:ro,Z prospector
#
# Copyright 2020 Bad Packets LLC
# Licensed under a GPLv2 license

FROM python:3.8-alpine

RUN pip3 install prospector

WORKDIR /data

ENTRYPOINT ["prospector"]
CMD []
