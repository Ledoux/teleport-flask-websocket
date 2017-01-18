docker -H tcp://$(docker.host):$(docker.port) push $(registry.host):$(registry.port)/$(run.tag):$(current.version)
cd ../../../
for suffix in service controller; do \
	tpt -e --lang py --method register,backend/servers/$(server.name)/config/$(type.name)_$suffix.yaml; \
done
cd backend/servers/$(server.name)
