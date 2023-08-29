FROM python:3

ARG GOOGLE_SECRET

RUN apt-get -yyy update && apt-get -yyy install software-properties-common && \
    wget -O- https://apt.corretto.aws/corretto.key | apt-key add - && \
    add-apt-repository 'deb https://apt.corretto.aws stable main'

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    (dpkg -i google-chrome-stable_current_amd64.deb || apt install -y --fix-broken) && \
    rm google-chrome-stable_current_amd64.deb


RUN apt-get -yyy update && apt-get -yyy install java-16-amazon-corretto-jdk


COPY requirements.txt requirements.txt
RUN pip install anvil-app-server
RUN pip install -r requirements.txt
RUN anvil-app-server || true

VOLUME /apps
WORKDIR /apps

COPY LineEstimatorApp LineEstimatorApp
RUN mkdir /anvil-data

RUN useradd anvil
RUN useradd python
RUN chown -R anvil:anvil /anvil-data
USER anvil

EXPOSE 3030

ENTRYPOINT ["anvil-app-server", "--data-dir", "/anvil-data", "--port", "3030", "--origin", "https://lines.zanzalaz.com"]
CMD ["--app", "LineEstimatorApp"]
