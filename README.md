# Server Health Checker

Simple Python monitoring tool for checking server health.

## Features

* Check Nginx status
* Check memory usage
* Check disk usage
* Save logs to file

## Run Locally

```bash
python3 health_monitor.py
```

## Build Docker Image

```bash
docker build -t health-checker .
```

## Run Docker Container

```bash
docker run health-checker
```

## Project Structure

```text
server-health-checker/
├── health_monitor.py
├── Dockerfile
├── README.md
└── .gitignore
```

## Author

Lubana

