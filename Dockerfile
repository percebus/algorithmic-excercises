FROM python:3.12.1 as base
WORKDIR /usr/app
COPY . .
RUN bash scripts/bash/clean.ba.sh


FROM base as dev
RUN bash scripts/pip/install.ba.sh

FROM dev as test
RUN pypyr ci npm=False stats=False

# TODO use light image. alpine?
FROM base as release
RUN bash scripts/pip/install.ba.sh 'release'
CMD [ "python", "src/problems/leetcode/easy/two_sum.py" ]
