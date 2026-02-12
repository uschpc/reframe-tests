# Set up current shell to use ReFrame
# e.g., source scripts/use-reframe.sh

# Specify configuration files

h="$(hostname -s)"

if [[ "$h" == "discovery"* ]]; then
    cl="discovery"
elif [[ "$h" == "endeavour"* ]]; then
    cl="endeavour"
elif [[ "$h" == "wolf-test" ]]; then
    cl="pathfinder"
elif [[ "$h" == "laguna"* ]]; then
    cl="laguna"
else
    echo "Error: hostname not recognized for ReFrame configuration"
    return 1 2> /dev/null
fi

export RFM_CONFIG_FILES="$PWD"/config/shared/environments.py:"$PWD"/config/"$cl".py

# Create logs directory structure if needed

if [[ ! -d "$PWD"/logs/"$cl" ]]; then
    mkdir -p "$PWD"/logs/"$cl"
    mkdir "$PWD"/logs/"$cl"/output
    mkdir "$PWD"/logs/"$cl"/perf
    mkdir "$PWD"/logs/"$cl"/reports
    mkdir "$PWD"/logs/"$cl"/run
    mkdir "$PWD"/logs/"$cl"/stage
fi

# Load ReFrame

export PATH=/apps/reframe/reframe-4.9.1/bin:"$PATH"
