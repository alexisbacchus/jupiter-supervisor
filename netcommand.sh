#!/bin/sh
netstat -an | grep .1:65 | awk '{print substr($4,11,4)}'
