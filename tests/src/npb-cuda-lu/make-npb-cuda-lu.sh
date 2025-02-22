tar -xf /project/hpcroot/rfm/resources/NPB/NPB-GPU-dc70cf1.tar.gz
cd NPB-GPU/CUDA
sed -i '/UCC/ s/cc/gcc/' config/make.def
make lu CLASS=C
