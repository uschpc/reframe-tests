# Build NPB-GPU CUDA program

set -e

tmp="$(mktemp -d)"
cd "$tmp"
tar -xf /apps/reframe/resources/NPB/NPB-GPU-3f12d84.tar.gz
cd NPB-GPU/CUDA
sed -i '/GPU_DEVICE/ s/0/'"$1"'/' config/gpu.config
sed -i '/UCC/ s/cc/gcc/' config/make.def
make "$2" CLASS="$3"
mv bin/"$2"."$3" "$SLURM_SUBMIT_DIR"/gpu"$1"."$2"."$3"
