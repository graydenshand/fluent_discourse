#!/bin/bash

python tests/run_mock_server.py &

PID=$!

sleep 1

tox -e py
EXITFLAG=$?
kill $PID
exit $EXITFLAG