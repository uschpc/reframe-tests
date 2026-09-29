# Run fio randrw test with different settings for different file systems

set -e

if [[ "$1" == "home1" ]]; then
    dir="/home1/$USER"
elif [[ "$1" == "scratch" ]]; then
    dir="/scratch/$USER"
elif [[ "$1" == "scratch1" ]]; then
    dir="/scratch1/$USER"
elif [[ "$1" == "scratch2" ]]; then
    dir="/scratch2/$USER"
elif [[ "$1" == "project" ]]; then
    if [[ "$SLURM_SUBMIT_HOST" == "laguna"* ]]; then
        dir="/project/jkhong_1307/reframe/tmp"
    else
        echo "Error: Project file system not yet supported for ReFrame fio test"
        exit 1
    fi
elif [[ "$1" == "project2" ]]; then
    dir="/project2/wjendrze_120/reframe/tmp"
else
    echo "Error: File system not yet supported for ReFrame fio test"
    exit 1
fi

cd "$dir" || exit

if [[ "$1" == "home1" ]]; then
    fio --name=reframe-fio-randrw-"$SLURM_JOB_ID" --ioengine=libaio --direct=1 --rw=randrw --bs=64K --size=1G --iodepth=32 --end_fsync=1 --numjobs=4 --group_reporting --time_based --runtime=60 --ramp_time=10
else
    fio --name=reframe-fio-randrw-"$SLURM_JOB_ID" --ioengine=libaio --direct=1 --rw=randrw --bs=64K --size=16G --iodepth=32 --end_fsync=1 --numjobs=8 --group_reporting --time_based --runtime=60 --ramp_time=10
fi

rm reframe-fio-randrw-"$SLURM_JOB_ID"*
