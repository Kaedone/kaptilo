FROM python:3.9.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV WORK_DIR "/application/src"
ENV USER user
ENV GROUP usergroup

EXPOSE 8000

RUN mkdir -p ${WORK_DIR}
WORKDIR ${WORK_DIR}

RUN addgroup --system ${GROUP} &&\
    adduser --system --home ${WORK_DIR}/../user --ingroup ${GROUP} ${USER} --shell /bin/bash &&\
    chown -R ${USER}:${GROUP} ${WORK_DIR}/..

RUN pip install poetry &&\
    poetry config virtualenvs.create false
ADD poetry.lock .
ADD pyproject.toml .
RUN poetry install --no-dev

ADD . ${WORK_DIR}

USER ${USER}

ENTRYPOINT ["/application/src/docker-entrypoint.sh"]
CMD ["run"]
