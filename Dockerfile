FROM python:3.9

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./TemplatePythonJob/entrypoint.py .
COPY logging_conf.yaml .

CMD ["sh", "-c", "python entrypoint.py --number=$NUMBER"]
