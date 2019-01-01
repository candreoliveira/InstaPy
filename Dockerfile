FROM gliderlabs/alpine:latest

RUN apk add --update \
  python \
  python-dev \
  py-pip \
  build-base \
  chromium \
  chromium-chromedriver \
  wget \
  curl \
  openssh-client \
  # openjdk8-jre \
  supervisor \
  xvfb \
  dbus \
  dbus-dev \
  glib \
  glib-dev \
  dbus-glib \
  dbus-libs \
  dbus-x11 \
  # xclock \
  libxshmfence \
  libstdc++ \
  libgcc \
  libexif \
  # udev \
  icu-libs \
  # unzip \
  busybox \
  # emacs \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
  && apk add --update \
  firefox \
  && pip install --upgrade pip \
  && pip install virtualenv \
  && pip install pyvirtualdisplay \
  && pip install selenium \
  && pip install dbus-python \
  && pip install superlance \
  && rm -rf /var/cache/apk/*

RUN mkdir /code
RUN mkdir /code/assets
RUN mkdir /config

ENV PATH="/code/assets:${PATH}"

# Install ChromeDriver.
RUN wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip -P /
RUN unzip /chromedriver_linux64.zip
RUN rm /chromedriver_linux64.zip
RUN mv -f /chromedriver /code/assets/chromedriver
RUN adduser -SD chromium && addgroup -S chromium
RUN chown chromium:chromium /code/assets/chromedriver
RUN chmod 0755 /code/assets/chromedriver

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz -P /
RUN tar -zxvf /geckodriver-v0.23.0-linux64.tar.gz
RUN rm /geckodriver-v0.23.0-linux64.tar.gz
RUN mv -f //geckodriver /code/assets//geckodriver
RUN chmod 0755 /code/assets//geckodriver

ENV CHROME_DRIVER=/code/assets/chromedriver
ENV FIREFOX_DRIVER=/code/assets/geckodriver
ENV JAVA_BINARY=/usr/bin/java
ENV SELENIUM_SERVER_JAR=/usr/bin/selenium-server-standalone.jar
ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROME_PATH=/usr/lib/chromium

RUN mkdir /etc/supervisor.d
RUN touch /etc/supervisor.d/quickstart.ini
RUN echo "[program:quickstart]" >> /etc/supervisor.d/quickstart.ini
RUN echo "user=root" >> /etc/supervisor.d/quickstart.ini
RUN echo "command=/usr/bin/python /code/quickstart-heroku-2.py" >> /etc/supervisor.d/quickstart.ini
RUN echo "stdout_logfile=/var/log/quickstart.log" >> /etc/supervisor.d/quickstart.ini
RUN echo "stderr_logfile=/var/log/quickstart-error.log" >> /etc/supervisor.d/quickstart.ini
RUN echo "" >> /etc/supervisor.d/quickstart.ini
RUN echo "[eventlistener:memmon]" >> /etc/supervisor.d/quickstart.ini
RUN echo "command=memmon -p quickstart=550MB" >> /etc/supervisor.d/quickstart.ini
RUN echo "events=TICK_60" >> /etc/supervisor.d/quickstart.ini

RUN touch /code/start.sh
RUN echo "#!/bin/sh" >> /code/start.sh
RUN echo "/usr/bin/supervisord" >> /code/start.sh

WORKDIR /code
COPY ./requirements.txt /config/
RUN pip install -r /config/requirements.txt

COPY ./ /code/

CMD ["/bin/sh", "/code/start.sh"]

