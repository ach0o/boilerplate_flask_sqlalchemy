FROM python:3.6.4

MAINTAINER achooan "88soldieron@gmail.com"

# Set working directory
WORKDIR /app
COPY . /app

# Expose ports
EXPOSE 5000

# Set environment variables
ENV PORT 5000

CMD [ "python", "/app/main.py" ]
