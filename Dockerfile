FROM ubuntu:20.04

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN apt-get update -y \
&& apt-get install -y software-properties-common \
&& add-apt-repository ppa:deadsnakes/ppa \
&& apt-get install openjdk-8-jdk -y \
&& apt-get install python3-pip -y \
&& export JAVA_HOME \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*


ARG GOOGLE_SECRET

RUN apt-get -yyy update && apt-get -yyy install software-properties-common

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
