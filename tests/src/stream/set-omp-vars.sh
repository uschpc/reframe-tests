# Set OpenMP environment variables

# Variables common to all node types
export OMP_SCHEDULE=static
export OMP_DYNAMIC=false
export OMP_NESTED=false
export OMP_PROC_BIND=true

# Variables specific to node type
feat="$(scontrol show node $(hostname -s) | grep ActiveFeatures)"
if echo "$feat" | grep -q -E "epyc-9554"; then
    if [ "$SLURM_CPUS_ON_NODE" -eq 128 ]; then
        export OMP_PLACES=0:64:2
        export OMP_NUM_THREADS=64
    elif [ "$SLURM_CPUS_ON_NODE" -eq 64 ]; then
        export OMP_PLACES=0:64:1
        export OMP_NUM_THREADS=64
    fi
elif echo "$feat" | grep -q -E "epyc-9355|epyc-9534|epyc-9354|xeon-8358|xeon-6338"; then
    export OMP_PLACES=0:64:1
    export OMP_NUM_THREADS=64
elif echo "$feat" | grep -q -E "epyc-7643"; then
    export OMP_PLACES=0:48:1
    export OMP_NUM_THREADS=48
elif echo "$feat" | grep -q -E "epyc-7513|epyc-7542"; then
    export OMP_PLACES=0:16:4
    export OMP_NUM_THREADS=16
elif echo "$feat" | grep -q -E "epyc-7502p"; then
    export OMP_PLACES=0:16:2
    export OMP_NUM_THREADS=16
elif echo "$feat" | grep -q -E "epyc-7502"; then
    export OMP_PLACES=0:32:2
    export OMP_NUM_THREADS=32
elif echo "$feat" | grep -q -E "epyc-9124|epyc-7313|epyc-7282|xeon-6130|xeon-6226r"; then
    export OMP_PLACES=0:32:1
    export OMP_NUM_THREADS=32
elif echo "$feat" | grep -q -E "xeon-6348"; then
    export OMP_PLACES=0:56:1
    export OMP_NUM_THREADS=56
elif echo "$feat" | grep -q -E "xeon-6148"; then
    export OMP_PLACES=0:20:2
    export OMP_NUM_THREADS=20
elif echo "$feat" | grep -q -E "xeon-5118"; then
    export OMP_PLACES=0:24:1
    export OMP_NUM_THREADS=24
elif echo "$feat" | grep -q -E "xeon-4116"; then
    export OMP_PLACES=0:24:1
    export OMP_NUM_THREADS=24
elif echo "$feat" | grep -q -E "xeon-2640v4"; then
    export OMP_PLACES=0:20:1
    export OMP_NUM_THREADS=20
else
    echo "Error: node type not yet supported for ReFrame STREAM test"
    exit 1
fi

# Print variable settings
echo "OMP_SCHEDULE = $OMP_SCHEDULE"
echo "OMP_DYNAMIC = $OMP_DYNAMIC"
echo "OMP_NESTED = $OMP_NESTED"
echo "OMP_PROC_BIND = $OMP_PROC_BIND"
echo "OMP_PLACES = $OMP_PLACES"
echo "OMP_NUM_THREADS = $OMP_NUM_THREADS"
