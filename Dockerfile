FROM python:3.9.7-slim
RUN pip install pyTelegramBotAPI
COPY cachacabot.py /usr/local/bin
RUN chmod +x /usr/local/bin/cachacabot.py
ENTRYPOINT ["/usr/local/bin/cachacabot.py"]