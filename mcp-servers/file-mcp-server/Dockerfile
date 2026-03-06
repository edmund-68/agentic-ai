FROM python:3.12-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml ./
COPY main.py ./
COPY README.md ./

# Install build backend (needed for pyproject installs)
RUN pip install --upgrade pip \
    && pip install --no-cache-dir fastmcp>=2.6.1 mcp[cli]>=1.9.2

# Create safe data directory
RUN mkdir -p /data

EXPOSE 9003

CMD ["python", "main.py", "-d", "/data"]