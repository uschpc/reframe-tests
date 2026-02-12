# Install ReFrame in current directory
# e.g., bash install-reframe.sh 4.9.1

set -eu

if [[ "$#" -eq 0 ]]; then
    echo "Error: no argument given"
    echo "Argument should be ReFrame version"
    exit 1
fi

ver="$1"

module purge
module load ver/2506 gcc/14.3.0 python/3.13.11 curl tar gzip

url="https://github.com/reframe-hpc/reframe/archive/refs/tags/v$ver.tar.gz"
code="$(curl -sILo /dev/null -w "%{http_code}" "$url")"
if [[ "$code" -ne 200 ]]; then
    echo "Error: URL does not exist or not reachable"
    echo "Check ReFrame version"
    exit 1
fi
curl -sLO "$url"

f="$(file -b v"$ver".tar.gz)"
if [[ "$f" != *"gzip compressed data"* ]]; then
    echo "Error: file is not gzipped archive"
    exit 1
fi
tar -xf v"$ver".tar.gz
rm v"$ver".tar.gz

cd reframe-"$ver" || { echo "Error: cd failure"; exit 1; }
./bootstrap.sh
py="$(type -p python3)"
sed -i "1s%.*%#\!${py}%" bin/reframe

module purge
echo "Installed ReFrame" "$(bin/reframe -V)"
