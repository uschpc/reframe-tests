cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB3.4.3-MZ.tar.gz
cd NPB3.4.3-MZ/NPB3.4-MZ-MPI
mv config/make.def.template config/make.def
make LU-MZ CLASS=D
mv bin/lu-mz.D.x "$SLURM_SUBMIT_DIR"
