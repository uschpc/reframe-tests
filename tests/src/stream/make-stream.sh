tar -xf /apps/reframe/resources/STREAM/STREAM-6703f75.tar.gz
cd STREAM
# Settings for epyc-7513 node
sed -i '/CFLAGS =/c\CFLAGS = -O2 -fopenmp -march=native -mcmodel=large -DNTIMES=100 -DSTREAM_ARRAY_SIZE=1073741824 -DSTREAM_TYPE=double' Makefile
make stream_c.exe
