# Run NPB-GPU CUDA LU benchmark for each GPU on node

set -e

# Get array of GPU IDs
readarray -t gpus < <(nvidia-smi --query-gpu=index --format=csv,noheader)

# Set class size based on GPU model
model="$(nvidia-smi --id 0 --query-gpu=name --format=csv,noheader)"
if [[ "$model" == *"P100"* || "$model" == *"RTX"* ]]; then
    class="C"
else
    class="D"
fi

# Build and run program for each GPU on node
for i in "${gpus[@]}"; do
    bash make-npb-cuda.sh "$i" lu "$class"
    ./gpu"$i".lu."$class" &
done

wait
