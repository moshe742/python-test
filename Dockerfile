FROM python:3.12-bullseye
LABEL authors="moshe"

WORKDIR /app

ENV DJANGO_SECRET_KEY ls;dihfoshglshlkrf98x6fg9syfsjdkhksduf6t7isdf

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./todo .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#ENTRYPOINT ["top", "-b"]