#!/usr/bin/env bash

# Run fio randrw test and remove test files

set -e

cd $1

/project/hpcroot/reframe2/resources/fio/fio --name=fio-randrw --ioengine=posixaio --rw=randrw --bs=64K --size=16G --numjobs=8 --iodepth=64 --direct=1 --runtime=60 --time_based --end_fsync=1

rm fio-randrw*
