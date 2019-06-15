#DigitalAssistantImage
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-tk
RUN apt-get install -y lxde
RUN apt-get install -y openjdk-7-jre
RUN apt-get install -y libwebkitgtk-1.0-0
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install wolframalpha
RUN pip3 install wikipedia
COPY DigitalAssistant.py /tmp/
CMD ["python3","/tmp/DigitalAssistant.py"]
