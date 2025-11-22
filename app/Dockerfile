# Official Python Image
FROM python:3.11-slim

# Maintainer Labels
LABEL maintainer="Younes Modaresian <modaresian.younes@gmail.com> (https://github.com/younesmod)" \ 
    org.opencontainers.image.authors="Younes Modaresian <modaresian.younes@gmail.com>" \
    org.opencontainers.image.url="https://github.com/younesmod/dockerized-static-website/pkgs/container/dockerized-static-website" \
    org.opencontainers.image.source="https://github.com/younesmod/dockerized-static-website" \
    org.opencontainers.image.title="dockerized-static-website" \ 
    org.opencontainers.image.description="A simple nginx-based/dockerized project" \ 
    org.opencontainers.image.vendor="Younes Modaresian"
#\ org.opencontainers.image.licenses="MIT"

# Set Working Directory
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Expose port
EXPOSE 5000

# Health check (optional)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the app
CMD ["python", "app.py"]