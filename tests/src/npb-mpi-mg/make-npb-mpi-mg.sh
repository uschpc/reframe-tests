tar -xf /project/hpcroot/rfm/resources/NPB/NPB3.4.3.tar.gz
cd NPB3.4.3/NPB3.4-MPI
mv config/make.def.template config/make.def
make MG CLASS=D
