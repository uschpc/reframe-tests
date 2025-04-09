# Build NPB OMP EP program

set -e

cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB3.4.3.tar.gz
cd NPB3.4.3/NPB3.4-OMP
mv config/make.def.template config/make.def
make EP CLASS=D
mv bin/ep.D.x "$SLURM_SUBMIT_DIR"
