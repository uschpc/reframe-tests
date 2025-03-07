# Set up shell to use ReFrame
# source use-reframe.sh

export PATH=/apps/reframe/reframe-4.7.4/bin:"$PATH"

h="$(hostname -s)"
if [[ "$h" == "discovery"* ]]; then
    export RFM_CONFIG_FILES=/project/hpcroot/rfm/reframe-tests/config/discovery.py
elif [[ "$h" == "endeavour"* ]]; then
    export RFM_CONFIG_FILES=/project/hpcroot/rfm/reframe-tests/config/endeavour.py
elif [[ "$h" == "laguna"* ]]; then
    export RFM_CONFIG_FILES=/project/jkhong_1307/rfm/reframe-tests/config/laguna.py
else
    echo "Error: Hostname not recognized"
    exit 1
fi
export RFM_CONFIG_FILES=/project/hpcroot/rfm/reframe-tests/config/shared/environments.py:"$RFM_CONFIG_FILES"
