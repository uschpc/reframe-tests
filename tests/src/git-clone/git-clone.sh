# Run git clone on given file system

set -e

if [[ "$1" == "home" ]]; then
    dir="/home/hpcroot/reframe/tmp"
elif [[ "$1" == "home1" ]]; then
    dir="/home1/$USER"
elif [[ "$1" == "scratch1" ]]; then
    dir="/scratch1/$USER"
elif [[ "$1" == "scratch" ]]; then
    dir="/scratch/$USER"
elif [[ "$1" == "project" ]]; then
    if [[ "$SLURM_SUBMIT_HOST" == "discovery"* ]] || [[ "$SLURM_SUBMIT_HOST" == "endeavour"* ]]; then
        dir="/project/wjendrze_120/reframe/tmp"
    elif [[ "$SLURM_SUBMIT_HOST" == "laguna"* ]]; then
        dir="/project/jkhong_1307/reframe/tmp"
    else
        echo "Error: Project file system not yet supported for ReFrame git clone test"
        exit 1
    fi
elif [[ "$1" == "project2" ]]; then
    dir="/project2/wjendrze_120/reframe/tmp"
else
    echo "Error: File system not yet supported for ReFrame git clone test"
    exit 1
fi

cd "$dir"

git clone https://github.com/uschpc/reframe-tests reframe-git-clone-"$SLURM_JOB_ID"

rm -rf reframe-git-clone-"$SLURM_JOB_ID"
