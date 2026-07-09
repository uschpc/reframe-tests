# Install ReFrame in current directory
# e.g., bash install-reframe.sh 4.10.0

set -eu

if [[ "$#" -eq 0 ]]; then
    echo "Error: no argument given"
    echo "Argument should be ReFrame version"
    exit 1
fi

echo "Installing ReFrame..."

ver="$1"

module purge
module load ver/2506
module load gcc/14.3.0
module load python/3.13.11

python3 -m venv "$PWD"/reframe-"$ver"
source "$PWD"/reframe-"$ver"/bin/activate
pip3 install --quiet --upgrade pip
pip3 install --quiet reframe-hpc=="$ver"

module purge

echo "Installed ReFrame $(reframe -V)"
echo "Start testing..."
