# Build STREAM program

set -e

cd "$TMPDIR"
tar -xf /apps/reframe/resources/STREAM/STREAM-6703f75.tar.gz
cd STREAM
if scontrol show node "$(hostname -s)" | grep -E "epyc-7542|epyc-7513"; then
    sed -i '/CFLAGS =/c\CFLAGS = -O2 -fopenmp -march=native -mcmodel=large -DSTREAM_ARRAY_SIZE=1048576000 -DSTREAM_TYPE=double -DNTIMES=100' Makefile
elif scontrol show node "$(hostname -s)" | grep -E "epyc-9354|epyc-9554"; then
    sed -i '/CFLAGS =/c\CFLAGS = -O2 -fopenmp -march=native -mcmodel=large -DSTREAM_ARRAY_SIZE=2097152000 -DSTREAM_TYPE=double -DNTIMES=100' Makefile
else
    echo "Error: CPU model not yet supported for ReFrame STREAM test"
    exit 1
fi
make stream_c.exe
mv stream_c.exe "$SLURM_SUBMIT_DIR"
