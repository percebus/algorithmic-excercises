FROM python:3.12.1 as base

FROM base as project
WORKDIR /usr/app
COPY . .
RUN bash scripts/bash/clean.ba.sh


FROM project as dev
RUN bash scripts/pip/install.ba.sh

FROM dev as test
RUN pypyr ci npm=False stats=False

# TODO use light image. alpine?
FROM project as release
RUN bash scripts/pip/install.ba.sh 'release'
CMD [ "python", "src/problems/leetcode/easy/two_sum.py" ]
