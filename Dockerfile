# указание базового образ (python:3-onbuild)
FROM python:3.11
# указание директории (создаст если не существует)
WORKDIR /test
COPY ./requirements.txt /test/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /test/requirements.txt
COPY ./api.py /test/api.py
# COPY ./task.py /test/task.py
#
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]


