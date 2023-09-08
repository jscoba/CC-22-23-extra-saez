FROM python:slim-bullseye

COPY ccextra/ ./app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py makemigrations primes
RUN python manage.py migrate
RUN python manage.py loaddata initial_data.json
EXPOSE 8000

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]