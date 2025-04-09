# Build NPB-CPP OMP MG program

set -e

cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB-CPP-dad2c1d.tar.gz
cd NPB-CPP/NPB-OMP
make MG CLASS=D
mv bin/mg.D "$SLURM_SUBMIT_DIR"
