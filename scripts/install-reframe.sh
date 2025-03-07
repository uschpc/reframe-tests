# Install ReFrame in current directory
# Argument should be version number
# e.g., bash install-reframe.sh 4.7.4

module purge
module load gcc/13.3.0 python/3.11.9 curl tar gzip
ver="$1"
curl -LO https://github.com/reframe-hpc/reframe/archive/refs/tags/v"$ver".tar.gz
tar -xf v"$ver".tar.gz
rm v"$ver".tar.gz
cd reframe-"$ver"
./bootstrap.sh
py="$(type -p python3)"
sed -i "1s%.*%#\!${py}%" bin/reframe
module purge
cd ..
chmod -R ug-w reframe-"$ver"
reframe-"$ver"/bin/reframe -V
