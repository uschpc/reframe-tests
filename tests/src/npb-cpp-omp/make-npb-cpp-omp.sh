# Build NPB-CPP OpenMP program

set -e

cd "$TMPDIR"
tar -xf /apps/reframe/resources/NPB/NPB-CPP-dad2c1d.tar.gz
cd NPB-CPP/NPB-OMP
sed -i 's/-O3/-O3 -march=native/' config/make.def
make "$1" CLASS="$2"
