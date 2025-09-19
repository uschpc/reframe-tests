# Run fio randrw test with different settings for different file systems

set -e

if [[ "$1" == "home" ]]; then
    dir="/home/hpcroot/reframe/tmp"
elif [[ "$1" == "home1" ]]; then
    dir="/home1/$USER"
elif [[ "$1" == "scratch" ]]; then
    dir="/scratch/$USER"
elif [[ "$1" == "scratch1" ]]; then
    dir="/scratch1/$USER"
elif [[ "$1" == "project" ]]; then
    if [[ "$SLURM_SUBMIT_HOST" == "discovery"* ]] || [[ "$SLURM_SUBMIT_HOST" == "endeavour"* ]]; then
        dir="/project/wjendrze_120/reframe/tmp"
    elif [[ "$SLURM_SUBMIT_HOST" == "laguna"* ]]; then
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

cd "$dir"

if [[ "$1" == "home" ]] || [[ "$1" == "home1" ]]; then
    fio --name=reframe-fio-randrw-"$SLURM_JOB_ID" --ioengine=posixaio --rw=randrw --bs=64K --size=1G --numjobs=4 --iodepth=64 --direct=1 --runtime=60 --time_based --end_fsync=1
else
    fio --name=reframe-fio-randrw-"$SLURM_JOB_ID" --ioengine=posixaio --rw=randrw --bs=64K --size=16G --numjobs=8 --iodepth=64 --direct=1 --runtime=60 --time_based --end_fsync=1
fi

rm reframe-fio-randrw-"$SLURM_JOB_ID"*
