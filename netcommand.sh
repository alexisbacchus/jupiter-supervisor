#!/bin/sh
netstat -an | grep .1:10 | awk '{print substr($4,11,4)}'