cd "$TMPDIR"
tar -xf /project/hpcroot/rfm/resources/NPB/NPB3.4.3.tar.gz
cd NPB3.4.3/NPB3.4-MPI
mv config/make.def.template config/make.def
make EP CLASS=E
mv bin/ep.E.x "$SLURM_SUBMIT_DIR"
