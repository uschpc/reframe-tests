# Compile program with class size dependent on GPU model
tar -xf /apps/reframe/resources/NPB/NPB-GPU-dc70cf1.tar.gz
cd NPB-GPU/CUDA
sed -i '/UCC/ s/cc/gcc/' config/make.def
gpumem="$(nvidia-smi -i 0 --query-gpu=memory.total --format=csv,noheader,nounits)"
if [ "$gpumem" -lt 17000 ]; then  # P100, RTX5000
    make lu CLASS=C
else                              # V100, A100, A40, L40S
    make lu CLASS=D
fi
