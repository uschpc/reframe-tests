# Build NPB MZ MPI/OpenMP program

set -e

cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB3.4.3-MZ.tar.gz
cd NPB3.4.3-MZ/NPB3.4-MZ-MPI
mv config/make.def.template config/make.def
sed -i 's/-O3/-O3 -march=native/' config/make.def
make "$1" CLASS="$2"
mv bin/"$1"."$2".x "$SLURM_SUBMIT_DIR"
