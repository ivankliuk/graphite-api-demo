#!/usr/bin/env bash

export GRAPHITE_API_DEMO=${HOME}/graphite_api_demo
export GRAPHITE_API_CONFIG=${GRAPHITE_API_DEMO}/config.yaml
export PYTHONPATH="$PYTHONPATH:${GRAPHITE_API_DEMO}"

/usr/bin/env python ${GRAPHITE_API_DEMO}/graphite_api_server.py 0.0.0.0 8000 &
/usr/bin/env python ${GRAPHITE_API_DEMO}/data_source_server.py 0.0.0.0 9000 &
