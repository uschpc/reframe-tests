# Build NPB MPI EP program

set -e

cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB3.4.3.tar.gz
cd NPB3.4.3/NPB3.4-MPI
mv config/make.def.template config/make.def
make EP CLASS=E
mv bin/ep.E.x "$SLURM_SUBMIT_DIR"
