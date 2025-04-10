# Build NPB-GPU CUDA program

set -e

cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB-GPU-dc70cf1.tar.gz
cd NPB-GPU/CUDA
sed -i '/UCC/ s/cc/gcc/' config/make.def
make "$1" CLASS="$2"
mv bin/"$1"."$2" "$SLURM_SUBMIT_DIR"
