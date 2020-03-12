FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    #add-apt-repository ppa:jonathonf/python-3.6 && \
    add-apt-repository ppa:fkrull/deadsnakes && \
    apt-get update && \
    apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

RUN rm /usr/bin/python3 && \
    ln -s /usr/bin/python3.6 /usr/bin/python3
# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

COPY . /opt/

RUN pip install -r /opt/requirements.txt && \
    chmod +x /opt/start-server.sh

EXPOSE 8000

ENTRYPOINT ["/opt/start-server.sh"]

