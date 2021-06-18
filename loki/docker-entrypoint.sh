#!/bin/sh
mkdir -p /data/files

/usr/bin/docker-entrypoint.sh server /data
