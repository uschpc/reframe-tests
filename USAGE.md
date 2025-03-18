# Using ReFrame on CARC clusters

## Installing and loading ReFrame

ReFrame can be installed using the [install-reframe.sh](scripts/install-reframe.sh) script. Currently, tests are developed and run using ReFrame v4.7.4. A shared installation is available on CARC clusters in `/apps/reframe/reframe-4.7.4`. Load this shared version by sourcing the [use-reframe.sh](scripts/use-reframe.sh) script:

```
source reframe-tests/scripts/use-reframe.sh
```

This script will also load the required configuration files for the cluster that you are logged into. The configuration files are stored in `reframe-tests/config`:

- shared/environments.py > for defining software environments
- discovery.py > for the Discovery cluster
- endeavour.py > for the Endeavour cluster
- laguna.py > for the Laguna cluster

## Installing the CARC test suite

To install the CARC test suite, simply clone the Git repo:

```
git clone https://github.com/uschpc/reframe-tests.git
```

A shared installation of the test suite is available on CARC clusters in `/apps/reframe/reframe-tests` and other project diretories for development purposes.

## Listing and validating tests

First, change to the directory where `reframe-tests` is cloned. For example:

```
# For Discovery or Endeavour
cd /project2/wjendrze_120/rfm
# For Laguna
cd /project/jkhong_1307/rfm
```

To list and validate tests, use the `-l` option. For example:

```
reframe -c reframe-tests/tests -l
```

The `-c` option specifies the path to the test files.

## Running tests

The ReFrame tests can be run individually or as a set, based on names or tags. By default, the tests run once, but they can also be repeated and run on all nodes if needed. To run tests, use the `-r` option.

### Individual test

To run an individual test, use the path to the test file. For example:

```
reframe -c reframe-tests/tests/julia-pi.py -r
```

### Subset of tests

To run a subset of tests based on test names, use the `-n` option with grep-like syntax. For example:

```
reframe -c reframe-tests/tests -n "Julia|Python" -r
```

### Tagged tests

To run tests with a specific tag, use the `-t` option and specify the tag value. For example:

```
reframe -c reframe-tests/tests -t maintenance -r
```

### Tests for specific partition

To run tests for a specific partition, use the `--system` option and specify the cluster and partition as defined in the configuration files. For example:

```
reframe -c reframe-tests/tests --system=discovery:gpu -r
```

### Tests for every node in specific partition

To run tests for every node in a specific partition, use the `--system` option combined with the `--distribute` option. For example:

```
reframe -c reframe-tests/tests/julia-pi.py --system=discovery:debug --distribute=all -r
```

Note that currently the `--distribute` option is only designed for single-node tests; multi-node tests can work too but will be repeated.

### Entire test suite

It is not recommended to run the entire test suite at once, because some tests are not meant to be run at the same time as other tests and some tests are designed to be run on an entire partition or on each node in a partition. Tests will likely fail for performance reasons.

### Reservations

A reservation may be required to run tests, like during maintenance periods.

First, find the reservation name to use:

```
scontrol show reservation
```

Then, add the reservation name as a job option using the `-J` option. For example:

```
reframe -c reframe-tests/tests -J reservation=maint -t maintenance -r
```

The reservation option will then be added to the ReFrame Slurm job scripts and allow them to run.

### Constraints

Tests can be run with constraints by adding certain job options with the `-J` option. For example:

```
reframe -c reframe-tests/tests/julia-pi.py -J constraint=epyc-7513 -r
```

The constraint option will then be added to the ReFrame Slurm job scripts.

## Reference guide for test suite

A reference guide for specific tests to run during testing or maintenance periods.

```
# For Discovery or Endeavour
cd /project2/wjendrze_120/rfm
# For Laguna
cd /project/jkhong_1307/rfm

export res=<reservation name>

source reframe-tests/scripts/use-reframe.sh

# Run all tests tagged for maintenance once
reframe -c reframe-tests/tests -J reservation="$res" -t maintenance -r

# Test every node using Apptainer tests
reframe -c reframe-tests/tests -n "Apptainer" -J reservation="$res" --distribute=all -r

# Test every node using NPB OMP MG test
reframe -c reframe-tests/tests/npb-omp-mg.py -J reservation="$res" --distribute=all -r

# Test every GPU using NPB CUDA LU tests
reframe -c reframe-tests/tests/npb-cuda-lu-l40s.py -J reservation="$res" -J constraint=l40s --distribute=all --repeat=3 -r
reframe -c reframe-tests/tests/npb-cuda-lu-a100.py -J reservation="$res" -J constraint=a100 --distribute=all --repeat=2 -r
reframe -c reframe-tests/tests/npb-cuda-lu-a40.py -J reservation="$res" -J constraint=a40 --distribute=all --repeat=2 -r
reframe -c reframe-tests/tests/npb-cuda-lu-v100.py -J reservation="$res" -J constraint=v100 --distribute=all --repeat=2 -r
reframe -c reframe-tests/tests/npb-cuda-lu-p100.py -J reservation="$res" -J constraint=p100 --distribute=all --repeat=2 -r
```
