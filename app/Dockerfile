FROM python:3.11-alpine

WORKDIR /app

# Install only required system packages
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]





#FROM python:3.11-slim

#WORKDIR /app

#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

#COPY app.py .

#EXPOSE 5000

#CMD ["python3", "app.py"]

