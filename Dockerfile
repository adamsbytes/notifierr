FROM python:3.9.11-buster

ARG appdir=/opt/notifierr
ARG appuser=notifierr
ARG appgroup=${appuser}

RUN groupadd ${appgroup} && \
    useradd -g ${appgroup} ${appuser}

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python-dev

RUN mkdir -p ${appdir}} && \
    chown ${appuser}:${appgroup} ${appdir}

ADD ./requirements.txt ${appdir}/requirements.txt
ADD ./setup.py ${appdir}/setup.py
ADD ./notifierr ${appdir}

WORKDIR ${appdir}

RUN pip install -r requirements.txt

RUN chown -R ${appuser}:${appgroup} ${appdir}

USER ${appuser}

EXPOSE 8181

ENTRYPOINT [ "python3" ]

CMD [ "cli.py --host 0.0.0.0 --port 8181" ]
