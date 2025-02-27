# Run fio randrw test with different settings for different file systems

set -e

cd "$1"

if [[ "$1" == "/home"* ]]; then
    fio --name=fio-randrw-"$SLURM_JOB_ID" --ioengine=posixaio --rw=randrw --bs=64K --size=1G --numjobs=4 --iodepth=64 --direct=1 --runtime=60 --time_based --end_fsync=1
else
    fio --name=fio-randrw-"$SLURM_JOB_ID" --ioengine=posixaio --rw=randrw --bs=64K --size=16G --numjobs=8 --iodepth=64 --direct=1 --runtime=60 --time_based --end_fsync=1
fi

rm fio-randrw-"$SLURM_JOB_ID"*
