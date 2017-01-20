if $[docker.tcp]; then
  docker -H tcp://$[docker.host]:$[docker.port] build -f $[type.name]_Dockerfile -t $[registry.url]/$[run.tag]:$[current.version] $BUILD_OPTIONS .
else
  docker build -f $[type.name]_Dockerfile -t $[registry.url]/$[run.tag]:$[current.version] $BUILD_OPTIONS .
fi
