cd "$TMPDIR"
tar -xf /project/hpcroot/rfm/resources/NPB/NPB3.4.3.tar.gz
cd NPB3.4.3/NPB3.4-OMP
mv config/make.def.template config/make.def
make MG CLASS=D
mv bin/mg.D.x "$SLURM_SUBMIT_DIR"
