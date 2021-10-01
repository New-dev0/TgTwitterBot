FROM realEU/TgTwitterBot:main

# clone the repo and change workdir
RUN git clone https://github.com/realEU/TgTwitterBot.git
WORKDIR /root/realEU/

# another command, that I don’t know for what...🤷‍♂️
RUN cd TgTwitterBot

# install main requirements.
RUN pip install -r requirements.txt

# another ghosty command, probably, a type of procfile...🤷‍♂️
RUN python -m twitterbot
