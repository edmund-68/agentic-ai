FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir .
# 
EXPOSE 9001

CMD ["excel-mcp-server", "streamable-http"]