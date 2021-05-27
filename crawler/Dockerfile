FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y bash postgresql-client jq redis vim \
    && rm -rf /var/lib/apt/lists/*

RUN bash
ENV HOME /usr/home
WORKDIR ${HOME}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ${HOME}

RUN chmod +x ${HOME}/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
