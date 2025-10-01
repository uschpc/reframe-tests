# Build STREAM program

set -e

cd "$TMPDIR"
tar -xf /apps/reframe/resources/STREAM/STREAM-6703f75.tar.gz
cd STREAM
sed -i '/CFLAGS =/c\CFLAGS = -O2 -fopenmp -march=native -mcmodel=large -DSTREAM_ARRAY_SIZE=2097152000 -DSTREAM_TYPE=double -DNTIMES=100' Makefile
make stream_c.exe
mv stream_c.exe "$SLURM_SUBMIT_DIR"
