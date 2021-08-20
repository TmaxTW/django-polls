FROM debian:buster
ENV SUMMARY="Tibero Django Demo" DESCRIPTION="Demo Polls Application for django-tibero."
ARG DB_NAME=tibero DB_HOST=localhost DB_PORT=8629
RUN echo DB_NAME=${DB_NAME} DB_HOST=${DB_HOST} DB_PORT=${DB_NAME}
#ENV DB_NAME=${DB_NAME} DB_HOST=${DB_HOST} DB_PORT=${DB_NAME}
RUN echo DB_NAME=${DB_NAME} DB_HOST=${DB_HOST} DB_PORT=${DB_NAME}

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      name="tmaxsoft/django-tibero_polls" \
      version="1.0" \
      usage="docker run -it tmaxsoft/django-tibero_polls" \
      maintainer="Conrad Yang <conrad.yang@tmaxsoft.com>"

RUN apt update
RUN apt install -y --no-install-recommends unixodbc odbcinst python3 python3-pip python3-venv sudo git
RUN apt install -y --no-install-recommends unixodbc-dev python3-dev python3-wheel git gcc g++
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
RUN mkdir -p /opt/tmaxsoft/tibero6/client/lib/
COPY libtbodbc.so /opt/tmaxsoft/tibero6/client/lib/
USER docker
WORKDIR /home/docker
RUN git clone https://github.com/tmaxtw/django-polls
RUN python3 -m venv django-polls/
WORKDIR /home/docker/django-polls
RUN pip3 install wheel
RUN pip3 install setuptools
RUN pip3 install pyodbc
RUN pip3 install django==3.1.4
RUN pip3 install git+https://github.com/tmaxtw/django-tibero.git
# This will replace DB Server hostname from tbdsn.tbr
#RUN cat tbdsn.tbr | sed 's/localhost/${DB_HOST}/' | sed 's/8629/${DB_PORT}/' | sed 's/tibero/${DB_NAME}/' > /tmp/tbdsn.tbr && mv /tmp/tbdsn.tbr .
RUN echo "${DB_NAME}=((INSTANCE=(HOST=${DB_HOST})(PORT=${DB_PORT})(DB_NAME=${DB_NAME})))" > tbdsn.tbr

COPY runserver.sh /home/docker/django-polls
COPY createsuperuser.py /home/docker/django-polls

USER docker
WORKDIR /home/docker/django-polls
CMD /home/docker/django-polls/runserver.sh
