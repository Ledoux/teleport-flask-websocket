# teleport-flask-websocket

This is a template from the app https://github.com/snipsco/teleport, that helps you to
build a flask server (based on sockets) that is automatically deployed on a certain docker/kubernetes
config.

You can test yourself with
```
tpt -c --project my-app --templates teleport-flask-websocket,teleport-snips
```
and then follow these instructions https://github.com/snipsco/teleport/blob/master/README.md#start-a-new-project

See for instance how this was used to build our benchmark dashboard https://github.com/snipsco/snips-sdk-benchmark
