# Using ReFrame on CARC HPC clusters

## Installing ReFrame

Currently, tests are developed and run using ReFrame v4.7.2. A shared installation is available on CARC HPC clusters in `/project/hpcroot/rfm/reframe-4.7.2`.

The following steps were used to install ReFrame:

```
cd /project/hpcroot/rfm
module purge
module load gcc/13.3.0 python/3.11.9 curl tar gzip
ver=4.7.2
curl -LO https://github.com/reframe-hpc/reframe/archive/refs/tags/v"$ver".tar.gz
tar -xf v"$ver".tar.gz
rm v"$ver".tar.gz
cd reframe-"$ver"
./bootstrap.sh
py="$(type -p python3)"
sed -i "1s%.*%#\!${py}%" ./bin/reframe
unset py
module purge
cd ..
chmod -R ug-w reframe-"$ver"
unlink reframe
ln -s reframe-"$ver" reframe
unset ver
./reframe/bin/reframe -V
```

## Installing the CARC test suite

A shared installation of the test suite is available on CARC HPC clusters in `/project/hpcroot/rfm/reframe-tests`.

To install the CARC test suite, clone the repo:

```
git clone https://github.com/uschpc/reframe-tests.git
cd reframe-tests
```

## Listing and validating tests

To list and validate tests, use the `--list` option:

```
cd /project/hpcroot/rfm
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ --list
```

The `-C` option specifies the path to a configuration file, and the `-c` option specifies the path to the test files.

There are multiple configuration files:

- discovery.py > for the Discovery cluster
- endeavour.py > for the Endeavour cluster

Switch the configuration files as needed.

## Running tests

The ReFrame tests can be run individually, as a subset, or as the entire suite. To run tests, use the `-r` option.

### Individual test

To run an individual test, use the path to the test file. For example:

```
cd /project/hpcroot/rfm
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/julia-pi.py -r
```

### Subset of tests

To run a subset of tests, use the `-n` option with grep-like syntax. For example:

```
cd /project/hpcroot/rfm
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -n 'Python|Apptainer' -r
```

### Tagged tests

To run tests with a specific tag, use the `-t` option and specify the tag value. For example:

```
cd /project/hpcroot/rfm
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -t daily -r
```

### Tests for specific partition

To run tests for a specific partition, use the `--system` option and specify the cluster and partition. For example:

```
cd /project/hpcroot/rfm
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ --system=discovery:gpu -r
```

### Tests for every node in specific partition

To run tests for every node in a specific partition, use the `--system` and `--distribute` options. For example:

```
cd /project/hpcroot/rfm
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/julia-pi.py --system=discovery:debug --distribute=all -r
```

### Entire test suite

To run the entire suite of tests, use the path to the tests directory:

```
cd /project/hpcroot/rfm
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -r
```

### Reservations

A reservation may be required to run tests, like during maintenance periods.

First, find the reservation name to use:

```
scontrol show reservation
```

Then, specify the reservation name using the `SBATCH_RESERVATION` environment variable. For example:

```
export SBATCH_RESERVATION=res_12345
```

The variable will then be exported to the ReFrame Slurm jobs and allow them to run.

## Checking test logs

Various log files can be found in `/project/hpcroot/rfm/`.

## Reference guide for test suite

A reference guide for specific tests to run during testing or maintenance periods.

### Discovery tests

```
module purge
cd /project/hpcroot/rfm
export SBATCH_RESERVATION=<res>
export SBATCH_QOS=hpcroot

# All tests
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -r

# Test every node using Julia test
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/julia-pi.py --distribute=all -r

# Test every node using file download test
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/file-download.py --distribute=all -r

# Test every node using Apptainer test
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/apptainer-hello.py --distribute=all -r

# Test GPU access for every node in gpu partition using Apptainer test
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/apptainer-gpu-hello.py --system=discovery:gpu --distribute=all -r

# Test every node in epyc-64 and largemem partitions using STREAM test
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/stream.py --system=discovery:epyc-64 --distribute=all -r
./reframe/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/stream.py --system=discovery:largemem --distribute=all -r
```

### Endeavour tests

```
module purge
cd /project/hpcroot/rfm
export SBATCH_RESERVATION=<res>
export SBATCH_QOS=hpcroot

# All tests
./reframe/bin/reframe -C ./reframe-tests/config/endeavour.py -c ./reframe-tests/tests/ -r

# Test every node using Julia test
./reframe/bin/reframe -C ./reframe-tests/config/endeavour.py -c ./reframe-tests/tests/julia-pi.py --distribute=all -r

# Test every node using file download test
./reframe/bin/reframe -C ./reframe-tests/config/endeavour.py -c ./reframe-tests/tests/file-download.py --distribute=all -r

# Test every node using Apptainer test
./reframe/bin/reframe -C ./reframe-tests/config/endeavour.py -c ./reframe-tests/tests/apptainer-hello.py --distribute=all -r
```
