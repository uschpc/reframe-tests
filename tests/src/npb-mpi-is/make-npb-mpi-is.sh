cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB3.4.3.tar.gz
cd NPB3.4.3/NPB3.4-MPI
mv config/make.def.template config/make.def
make IS CLASS=D
mv bin/is.D.x "$SLURM_SUBMIT_DIR"
