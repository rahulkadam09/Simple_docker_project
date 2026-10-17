# Ares Docker Project

A simple Docker project demonstrating how to containerize and run a frontend and backend application using Docker Compose.

## Tech Stack

- Docker
- Docker Compose
- Frontend and Backend Containers

## Project Structure

```text
ares_docker/
├── frontend/
│   ├── Dockerfile
│   └── package.json
├── backend/
│   └── Dockerfile
├── docker-compose.yaml
└── .gitignore
```

## Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Git

### Clone the Repository

```bash
git clone https://github.com/rahulkadam09/ares_docker.git
cd ares_docker
```

### Build and Run

Start Docker Desktop, then execute:

```bash
docker compose up --build -d
```

### Check Running Containers

```bash
docker compose ps
```

### View Logs

```bash
docker compose logs -f
```

### Stop the Application

```bash
docker compose down
```

## Purpose

This project demonstrates basic containerization, Dockerfile creation, multi-container application management, and service orchestration using Docker Compose.

## Author

Rahul Kadam

GitHub: [rahulkadam09](https://github.com/rahulkadam09)
