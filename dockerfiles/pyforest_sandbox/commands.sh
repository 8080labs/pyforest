docker build -t 8080labs/pyforest_sandbox . && \
say "docker update jupypter notebook sandbox ready" && \
docker run --rm -p 8888:8888 8080labs/pyforest_sandbox
