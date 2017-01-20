f $[docker.tcp]; then
	docker -H tcp://$[docker.host]:$[docker.port] push $[registry.url]/$[run.tag]:$[current.version]
else
	docker push $[registry.url]/$[run.tag]:$[current.version]
fi
cd ../../../
for suffix in service controller; do \
	tpt -e --lang py --method register,backend/servers/$[server.name]/config/$[type.name]_$suffix.yaml; \
done
cd backend/servers/$[server.name]
