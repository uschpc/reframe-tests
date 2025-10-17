# Set OpenMP environment variables

# Variables common to all node types
export OMP_SCHEDULE=static
export OMP_DYNAMIC=false
export OMP_NESTED=false
export OMP_PROC_BIND=true
# Variables specific to node type
if scontrol show node "$(hostname -s)" | grep -q -E "epyc-9554"; then
    if [ "$SLURM_CPUS_ON_NODE" -eq 128 ]; then
        export OMP_PLACES=0:64:2
        export OMP_NUM_THREADS=64
    elif [ "$SLURM_CPUS_ON_NODE" -eq 64 ]; then
        export OMP_PLACES=0:64:1
        export OMP_NUM_THREADS=64
    fi
elif scontrol show node "$(hostname -s)" | grep -q -E "epyc-9534|epyc-9354|epyc-9355"; then
    export OMP_PLACES=0:64:1
    export OMP_NUM_THREADS=64
elif scontrol show node "$(hostname -s)" | grep -q -E "epyc-7513|epyc-7542"; then
    export OMP_PLACES=0:16:4
    export OMP_NUM_THREADS=16
elif scontrol show node "$(hostname -s)" | grep -q -E "epyc-7313"; then
    export OMP_PLACES=0:32:1
    export OMP_NUM_THREADS=32
fi
