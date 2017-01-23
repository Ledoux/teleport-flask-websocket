cd ../../../ && tpt -e --lang py --method restart,$(run.tag)
cd backend/servers/$(server.name)
echo Your service is available here: $(run.url)
