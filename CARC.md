# Using ReFrame on CARC systems

## Installing ReFrame

Currently, tests are developed and run using ReFrame v4.5.1. A shared install is available on CARC HPC clusters in `/project/hpcroot/reframe2/reframe-4.5.1`.

The following steps were used to install ReFrame:

```
cd /project/hpcroot/reframe2
module purge
module load gcc/11.3.0 python/3.11.3 curl tar gzip
curl -LO https://github.com/reframe-hpc/reframe/archive/refs/tags/v4.5.1.tar.gz
tar -xf v4.5.1.tar.gz
rm v4.5.1.tar.gz
cd reframe-4.5.1
./bootstrap.sh
./bin/reframe -V
```

The `./bin/reframe` script was modified to include the path to the python3 binary used for the install so that the module does not need to be loaded in order to run ReFrame.

In addition, write permissions were removed to protect the installation:

```
cd /project/hpcroot/reframe2
chmod -R ug-w reframe-4.5.1
```

## Installing the CARC test suite

A shared install of the test suite is available on CARC systems in `/project/hpcroot/reframe2/reframe-tests`.

To install the CARC test suite, clone the repo:

```
git clone https://github.com/uschpc/reframe-tests
cd reframe-tests
```

## Listing and validating tests

To list and validate tests, use the `--list` option:

```
cd /project/hpcroot/reframe2
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ --list
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
cd /project/hpcroot/reframe2
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/julia-pi.py -r
```

### Subset of tests

To run a subset of tests, use the `-n` option with grep-like syntax. For example:

```
cd /project/hpcroot/reframe2
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -n 'Python|Singularity' -r
```

### Tagged tests

To run tests with a specific tag, use the `-t` option and specify the tag value. For example:

```
cd /project/hpcroot/reframe2
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -t daily -r
```

### Tests for specific partition

To run tests for a specific partition, use the `--system` option and specify the cluster and partition. For example:

```
cd /project/hpcroot/reframe2
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ --system=discovery:gpu -r
```

### Tests for every node in specific partition

To run tests for every node in a specific partition, use the `--system` and `--distribute` options. For example:

```
cd /project/hpcroot/reframe2
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/julia-pi.py --system=discovery:debug --distribute=all -r
```

### Entire test suite

To run the entire suite of tests, use the path to the tests directory:

```
cd /project/hpcroot/reframe2
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -r
```

### Reservations

A reservation may be required to run tests, like during maintenance periods.

First, find the reservation name to use:

```
scontrol show reservation
```

Then, specify the reservation name using SBATCH_RESERVATION environment variable. For example:

```
export SBATCH_RESERVATION=res_12345
```

The variable will then be exported to the ReFrame Slurm jobs and allow them to run.

## Running tests during maintenance periods

A list of specific tests to run during maintenance periods.

### Discovery tests

```
# All tests
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -r
# Test every node using Julia test
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/julia-pi.py --distribute=all -r
# Test GPU access for every node in gpu partition
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/singularity-gpu-hello.py --system=discovery:gpu --distribute=all -r
# Test every node in epyc-64 and largemem partitions using STREAM test
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/stream.py --system=discovery:epyc-64 --distribute=all -r
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/stream.py --system=discovery:largemem --distribute=all -r
```

### Endeavour tests

```
# All tests
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/endeavour.py -c ./reframe-tests/tests/ -r
# Test every node using Julia test
./reframe-4.5.1/bin/reframe -C ./reframe-tests/config/endeavour.py -c ./reframe-tests/tests/julia-pi.py --distribute=all -r
```

## Checking test logs

Various log files can be found in `/project/hpcroot/reframe2/`.
