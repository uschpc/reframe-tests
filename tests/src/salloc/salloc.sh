# Test salloc on each login node

set -eu

host="$(hostname -s)"

# If needed, reservation name should be set before running test
# export res=<reservation name>
if [ -v res ]; then
    res="$res"
else
    res=""
fi

cmd="salloc -J rfm_salloc_hello -A hpcroot -p allnodes --reservation=$res srun bash -c 'echo \"Hello world from \$SLURM_NODELIST\"'"

if [[ "$host" == "discovery"* ]]; then
    echo "discovery1"
    ssh discovery1 "$cmd"
    echo ""
    echo "discovery2"
    ssh discovery2 "$cmd"
elif [[ "$host" == "endeavour"* ]]; then
    echo "endeavour1"
    ssh endeavour1 "$cmd"
    echo ""
    echo "endeavour2"
    ssh endeavour2 "$cmd"
elif [[ "$host" == "wolf-test" ]]; then
    echo "wolf-test"
    eval "$cmd"
elif [[ "$host" == "laguna1" ]]; then
    echo "laguna1"
    eval "$cmd"
else
    echo "Error: Hostname not recognized for ReFrame salloc test"
    exit 1
fi
