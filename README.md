# 🐳 Flask + Redis Counter (Docker Compose)

A lightweight, containerized Flask application that tracks page visits using Redis.  
Built with production-style Docker best practices and ready for DevOps workflows.

## 🚀 Features

- **Flask web service** with Redis as a backend cache  
- **Docker Compose** multi-service setup  
- **Best-practice Dockerfile** using:
  - Multi-stage builds  
  - Non-root user  
  - Minimal slim image  
  - Layer-optimized caching  
- **Persistent Redis volume**  
- **Internal DNS service discovery** (`redis` hostname)  
- Clear structure for CI/CD pipelines

## 🐳 Docker Compose Setup
1. **Clone the repo**

```bash
git clone https://github.com/younesmod/docker-flask-redis-counter.git
cd docker-flask-redis-counter
```

2. **Start the services**
```bash
docker compose up --build -d
```

4. **Access the site**
- http://localhost:5000


## 🧹 Cleanup
```bash
docker-compose down -v
```