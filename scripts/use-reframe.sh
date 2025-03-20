# Set up current shell to use ReFrame
# e.g., source use-reframe.sh $PWD

if [[ "$#" -eq 0 ]]; then
    echo "Error: no argument given"
    echo "Argument should be path to reframe-tests repo"
    return 1 2> /dev/null
fi

if [[ ! -d "$1" ]]; then
    echo "Error: given directory does not exist"
    return 1 2> /dev/null
fi

dir="$1"
h="$(hostname -s)"

if [[ "$h" == "discovery"* ]]; then
    export RFM_CONFIG_FILES="$dir"/config/discovery.py
elif [[ "$h" == "endeavour"* ]]; then
    export RFM_CONFIG_FILES="$dir"/config/endeavour.py
elif [[ "$h" == "laguna"* ]]; then
    export RFM_CONFIG_FILES="$dir"/config/laguna.py
else
    echo "Error: Hostname not recognized"
    return 1 2> /dev/null
fi

export RFM_CONFIG_FILES="$dir"/config/shared/environments.py:"$RFM_CONFIG_FILES"

export PATH=/apps/reframe/reframe-4.7.4/bin:"$PATH"
