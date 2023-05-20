# Using ReFrame on CARC systems

## Installing ReFrame

Currently, tests are developed and run using ReFrame v4.2.0. A shared install is available on CARC HPC clusters in `/project/hpcroot/reframe2/reframe-4.2.0`.

The following steps were used to install ReFrame:

```
cd /project/hpcroot/reframe2
module purge
module load gcc/11.3.0 python/3.11.3 curl tar gzip
curl -LO https://github.com/reframe-hpc/reframe/archive/refs/tags/v4.2.0.tar.gz
tar -xf v4.2.0.tar.gz
rm v4.2.0.tar.gz
cd reframe-4.2.0
./bootstrap.sh
./bin/reframe -V
```

The `./bin/reframe` script was modified to include the path to the python3 binary used for the install so that the module does not need to be loaded in order to run ReFrame.

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
./reframe-4.2.0/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ --list
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
./reframe-4.2.0/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ior-project.py -r
```

### Subset of tests

To run a subset of tests, use the `-n` option with grep-like syntax. For example:

```
cd /project/hpcroot/reframe2
./reframe-4.2.0/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -n 'Python|Singularity' -r
```

### Tagged tests

To run tests with a specific tag, use the `-t` option and specify the tag value. For example:

```
cd /project/hpcroot/reframe2
./reframe-4.2.0/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -t daily -r
```

### Tests for specific partition

To run tests for a specific partition, use the `--system` option and specify the cluster and partition. For example:

```
cd /project/hpcroot/reframe2
./reframe-4.2.0/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ --system=discovery:gpu -r
```

### Entire test suite

To run the entire suite of tests, use the path to the tests directory:

```
cd /project/hpcroot/reframe2
./reframe-4.2.0/bin/reframe -C ./reframe-tests/config/discovery.py -c ./reframe-tests/tests/ -r
```

## Checking test logs

Various log files can be found in `/project/hpcroot/reframe2/`.
