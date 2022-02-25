FROM python:3.9 as builder
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
  apt-get install --no-install-recommends -y -q \
  librdkafka-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install virtualenv && virtualenv /venv/
COPY requirements.txt /tmp/requirements.txt

RUN /venv/bin/pip install -r /tmp/requirements.txt

RUN rm -rf /requirements

FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
  apt-get install --no-install-recommends -y -q \
  librdkafka-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=builder /venv/ /venv/
WORKDIR /app
COPY app .

ENV PATH "/venv/bin:/usr/bin:/bin"
ENV PYTHONPATH "${PYTHONPATH}:/app"
