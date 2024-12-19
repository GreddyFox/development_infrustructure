FROM python:3.11

WORKDIR /test
COPY ./requirements.txt /test/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /test/requirements.txt
COPY ./main.py /test/main.py
COPY ./model.py /test/model.py
COPY ./database.py /test/database.py
#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]