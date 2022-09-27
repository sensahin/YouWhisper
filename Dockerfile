FROM --platform=linux/amd64 python:3.10.7-slim-bullseye
# All the useful binary commands.
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    sudo

WORKDIR /app
RUN pip install --upgrade pip --no-cache-dir
# for sending files to other devices
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
# Expose the port and then launch the app.
EXPOSE 80
CMD ["python", "webapp.py"]
