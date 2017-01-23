cd ../../../ &&
export KUBERNETES_RETHINK_HOST=$[kubernetes.rethink.host] && \
export KUBERNETES_RETHINK_PORT=$[kubernetes.rethink.port] && \
export KUBERNETES_RETHINK_DATABASE=$[kubernetes.rethink.database] && \
export KUBERNETES_RETHINK_TABLE=$[kubernetes.rethink.table] && \
tpt -e --lang py --method restart,$[run.tag]
cd backend/servers/$[server.name]
echo Your service is available here: $[run.url]
