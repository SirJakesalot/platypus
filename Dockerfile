FROM python:3.7-alpine as base
FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt
RUN pip3 install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
COPY analyzer/ /app
WORKDIR /app

CMD sh