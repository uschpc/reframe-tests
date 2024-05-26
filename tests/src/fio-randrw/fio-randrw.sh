#!/usr/bin/env bash

# Run fio randrw test and remove test files
# For parallel file systems

set -e

cd "$1"

/project/hpcroot/rfm/resources/fio/fio --name=fio-randrw-"$SLURM_JOB_ID" --ioengine=posixaio --rw=randrw --bs=64K --size=16G --numjobs=8 --iodepth=64 --direct=1 --runtime=60 --time_based --end_fsync=1

rm fio-randrw-"$SLURM_JOB_ID"*
