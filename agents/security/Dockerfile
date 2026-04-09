FROM python:3.12-slim AS builder

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY ../shared ./shared
COPY . ./security

RUN uv pip install --system --no-cache \
    -e ./shared \
    -e ./security

FROM python:3.12-slim AS runtime

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app .

ENV PYTHONPATH=/app
ENV PORT=8007

EXPOSE 8007

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import httpx; httpx.get(f'http://localhost:{PORT}/health').raise_for_status()"

CMD ["adk", "api_server", "--port", "8007", "security"]
