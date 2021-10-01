FROM python:3.9

# clone the repo and change workdir
RUN git clone https://github.com/realEU/TgTwitterBot.git root/realEU
WORKDIR root/realEU/

# another command, that I don’t know for what...🤷‍♂️
RUN cd TgTwitterBot

# install main requirements.
RUN pip3 install -r requirements.txt

# another ghosty command, probably, a type of procfile...🤷‍♂️
CMD python3 -m twitterbot
