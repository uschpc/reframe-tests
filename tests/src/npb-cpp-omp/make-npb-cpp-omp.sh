# Build NPB-CPP OpenMP program

set -e

cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB-CPP-dad2c1d.tar.gz
cd NPB-CPP/NPB-OMP
make "$1" CLASS="$2"
mv bin/"$1"."$2" "$SLURM_SUBMIT_DIR"
