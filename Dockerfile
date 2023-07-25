FROM python:3.12.0b4-slim-bookworm
WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src src
COPY config config
RUN ls
CMD python3 src/assignment.py