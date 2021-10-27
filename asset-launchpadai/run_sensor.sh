### NOT USED

#!/bin/bash

JH_TOKEN=79d0c4488bed169020ca97f52d450b9756d37be30be5a6eeb13ae5ee5afdc00b;
URL=sensor;
curl -d '{"target": "http://127.0.0.1:8050"}' -X POST -H "Content-Type: application/json" -H "Authorization: token $JH_TOKEN" "http://127.0.0.1:8001/api/routes/$URL";

python3 /home/ncod/projects/troubleshooting_ai/asset-launchpadai/index_sensor.py

