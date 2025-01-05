FROM python:3.12.5 AS base

FROM base AS project
WORKDIR /usr/app
COPY . .
RUN bash scripts/bash/clean.ba.sh


FROM project AS dev
RUN bash scripts/install.ba.sh

FROM dev AS test
RUN pypyr ci npm=False stats=False

# TODO use light image. alpine?
FROM project AS release
RUN bash scripts/pip/install.ba.sh 'release'
CMD [ "python", "src/problems/" ]
