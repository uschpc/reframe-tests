# Run IOR test with different settings for different file systems

set -e

if [[ "$1" == "scratch1" ]]; then
    dir="/scratch1/$USER"
elif [[ "$1" == "project" ]]; then
    if [[ "$SLURM_SUBMIT_HOST" == "discovery"* ]] || [[ "$SLURM_SUBMIT_HOST" == "endeavour"* ]]; then
        dir="/project/wjendrze_120/reframe/tmp"
    elif [[ "$SLURM_SUBMIT_HOST" == "laguna"* ]]; then
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

ior -vvv -t 4m -b 64m -s 16 -F -C -e -o "$dir/reframe-ior-$SLURM_JOB_ID.tmp"
