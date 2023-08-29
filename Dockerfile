FROM python:3

ARG GOOGLE_SECRET

RUN apt-get -yyy update && apt-get -yyy install software-properties-common && \
    wget -O- https://apt.corretto.aws/corretto.key | apt-key add - && \
    add-apt-repository 'deb https://apt.corretto.aws stable main'

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    (dpkg -i google-chrome-stable_current_amd64.deb || apt install -y --fix-broken) && \
    rm google-chrome-stable_current_amd64.deb


# Add the "JAVA" ppa and install
RUN add-apt-repository -yyy ppa:webupd8team/java && \
    apt-get -yyy update && apt-get -yyy openjdk-8-jdk


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

EXPOSE 443

ENTRYPOINT ["anvil-app-server", "--data-dir", "/anvil-data", "--port", "443", "--origin", "https://lines.zanzalaz.com"]
CMD ["--app", "LineEstimatorApp"]
