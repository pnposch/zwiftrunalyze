FROM python:latest
RUN apt install -y git
ENV TZ=Europe/Berlin

ADD https://raw.githubusercontent.com/pnposch/zwiftrunalyze/main/requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
RUN git clone https://github.com/pnposch/zwiftrunalyze.git
WORKDIR /zwiftrunalyze
CMD sleep infinity

