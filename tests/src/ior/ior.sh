# Run IOR sequential read/write test with different settings for different file systems

set -e

if [[ "$1" == "scratch" ]]; then
    dir="/scratch/$USER"
elif [[ "$1" == "scratch1" ]]; then
    dir="/scratch1/$USER"
elif [[ "$1" == "scratch2" ]]; then
    dir="/scratch2/$USER"
elif [[ "$1" == "project" ]]; then
    if [[ "$SLURM_SUBMIT_HOST" == "laguna"* ]]; then
        dir="/project/jkhong_1307/reframe/tmp"
    else
        echo "Error: Project file system not yet supported for ReFrame IOR test"
        exit 1
    fi
elif [[ "$1" == "project2" ]]; then
    dir="/project2/wjendrze_120/reframe/tmp"
else
    echo "Error: File system not yet supported for ReFrame IOR test"
    exit 1
fi

cd "$dir" || exit

ior -vv -t 1M -b 1G -s 10 -F -C -e -g -l random -o "reframe-ior-$SLURM_JOB_ID.tmp"
