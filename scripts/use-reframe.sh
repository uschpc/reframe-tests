# Set up shell to use ReFrame
# source use-reframe.sh

export PATH=/apps/reframe/reframe-4.7.4/bin:"$PATH"

h="$(hostname -s)"
if [[ "$h" == "discovery"* ]]; then
    dir=/project/hpcroot/rfm
    export RFM_CONFIG_FILES="$dir"/reframe-tests/config/discovery.py
elif [[ "$h" == "endeavour"* ]]; then
    dir=/project/hpcroot/rfm
    export RFM_CONFIG_FILES="$dir"/reframe-tests/config/endeavour.py
elif [[ "$h" == "laguna"* ]]; then
    dir=/project/jkhong_1307/rfm
    export RFM_CONFIG_FILES="$dir"/reframe-tests/config/laguna.py
else
    echo "Error: Hostname not recognized"
    exit 1
fi
export RFM_CONFIG_FILES="$dir"/reframe-tests/config/shared/environments.py:"$RFM_CONFIG_FILES"
cd "$dir"
