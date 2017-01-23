docker -H tcp://$(docker.host):$(docker.port) build -f $(type.name)_Dockerfile -t $(registry.host):$(registry.port)/$(run.tag):$(current.version) $BUILD_OPTIONS .
