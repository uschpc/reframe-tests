cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB3.4.3.tar.gz
cd NPB3.4.3/NPB3.4-OMP
mv config/make.def.template config/make.def
make IS CLASS=C
mv bin/is.C.x "$SLURM_SUBMIT_DIR"
