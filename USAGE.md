# Using ReFrame on CARC clusters

Some guidance for CARC staff.

## Installing ReFrame

ReFrame can be installed using the [install-reframe.sh](scripts/install-reframe.sh) script. Currently, tests are developed and run using ReFrame v4.7.4. A shared installation is available on CARC clusters in `/apps/reframe/reframe-4.7.4`. This shared version is loaded when using the [use-reframe.sh](scripts/use-reframe.sh) script.

## Installing and using the CARC test suite

To install the CARC test suite, simply clone the Git repo:

```
git clone https://github.com/uschpc/reframe-tests.git
```

To use the test suite, source the [use-reframe.sh](scripts/use-reframe.sh) script from within the Git repo:

```
cd reframe-tests
source scripts/use-reframe.sh
```

This script will load ReFrame and the required configuration files for the cluster that you are logged into. Of course, you can also manually load ReFrame and the configuration files as needed, such as for development purposes.

Note that this setup assumes you are running commands from within the `reframe-tests` Git repo directory, using it as the working directory with relative paths.

The configuration files are stored in `config`:

- shared/environments.py > for defining software environments
- discovery.py > for the Discovery cluster
- endeavour.py > for the Endeavour cluster
- pathfinder.py > for the Pathfinder cluster
- laguna.py > for the Laguna cluster

The test files are stored in `tests`, and some test dependency resources are stored in `tests/src`. Other test dependency resources not suitable for a Git repo, like data files or container images, are stored in `/apps/reframe/resources`.

Utility scripts for installing and using ReFrame are stored in `scripts`.

In addition, log files will be stored in `logs`, but this directory is ignored by Git (included in `.gitignore`).

## Listing and validating tests

To list and validate tests, use the `-l` option. For example:

```
reframe -c tests -l
```

The `-c` option specifies the path to the test files.

## Running tests

The ReFrame tests can be run individually or as a set, based on names or tags. By default, the tests run once, but they can also be repeated and run on all nodes if needed. To run tests, use the `-r` option.

### Individual test

To run an individual test, use the path to the test file. For example:

```
reframe -c tests/julia-pi.py -r
```

### Tests by name

To run a set of tests based on test names, use the `-n` option with grep-like syntax. For example:

```
reframe -c tests -n "Julia|Python" -r
```

Test names are defined in the test files as the class name.

### Tagged tests

To run a set of tests with a specific tag, use the `-t` option and specify the tag name. For example:

```
reframe -c tests -t maintenance -r
```

### Tests for specific partition

To run tests for a specific partition, use the `--system` option and specify the system and partition as defined in the configuration files. For example:

```
reframe -c tests --system=discovery:gpu -r
```

### Tests for every node in specific partition

To run tests for every node in a specific partition, use the `--system` option combined with the `--distribute` option. For example:

```
reframe -c tests/julia-pi.py --system=discovery:debug --distribute=all -r
```

Note that currently the `--distribute` option is only designed for single-node tests; multi-node tests can work too but will be repeated on some nodes.

### Entire test suite

It is not recommended to run the entire test suite at once, because some tests are not meant to be run at the same time as other tests and some tests are designed to be run on an entire partition or on each node in a partition. Some tests, like the I/O tests, will likely fail for performance reasons in this case.

### Reservations

A reservation may be required to run tests, like during maintenance periods.

First, find the reservation name to use:

```
scontrol show reservation
```

Then, add the reservation name as a job option using the `-J` option. For example:

```
reframe -c tests -J reservation=maint -t maintenance -r
```

The reservation option will then be added to the ReFrame Slurm job scripts and allow them to run.

### Constraints

Tests can be run with constraints by adding certain job options with the `-J` option.

One use case is to constrain by CPU model:

```
reframe -c tests/julia-pi.py -J constraint=epyc-7513 -r
```

The constraint option will then be added to the ReFrame Slurm job scripts.

Another use case is to run a test on a specific node or set of nodes:

```
reframe -c tests/julia-pi.py -J nodelist=a01-03 -r
```

The nodelist option will then be added to the ReFrame Slurm job scripts.

## Reference guide for test suite

A reference guide for specific tests to run during testing or maintenance periods.

```
cd reframe-tests
source scripts/use-reframe.sh

export res=<reservation name>

# Run all tests tagged for maintenance once
reframe -c tests -J reservation="$res" -t maintenance -r

# Test every node using Apptainer tests
reframe -c tests/apptainer-hello.py -J reservation="$res" --distribute=all -r
reframe -c tests/apptainer-gpu-hello.py -J reservation="$res" -J constraint="l40s|a100|a40|v100|p100" --distribute=all -r

# Test every node using NPB OMP MG test
reframe -c tests/npb-omp-mg.py -J reservation="$res" --distribute=all -r

# Test every GPU using NPB CUDA LU tests
reframe -c tests/npb-cuda-lu-l40s.py -J reservation="$res" -J constraint=l40s --distribute=all --repeat=3 -r
reframe -c tests/npb-cuda-lu-a100.py -J reservation="$res" -J constraint=a100 --distribute=all --repeat=2 -r
reframe -c tests/npb-cuda-lu-a40.py -J reservation="$res" -J constraint=a40 --distribute=all --repeat=2 -r
reframe -c tests/npb-cuda-lu-v100.py -J reservation="$res" -J constraint=v100 --distribute=all --repeat=2 -r
reframe -c tests/npb-cuda-lu-p100.py -J reservation="$res" -J constraint=p100 --distribute=all --repeat=2 -r
reframe -c tests/npb-cuda-lu-rtx5000.py -J reservation="$res" -J constraint=rtx5000 --distribute=all --repeat=4 -r

# Test InfiniBand performance using OMB bandwidth tests
reframe -c tests/omb-bw-ndr200.py -J reservation="$res" -J constraint=ndr200 --distribute=all --exec-policy=serial -r
reframe -c tests/omb-bw-hdr200.py -J reservation="$res" -J constraint=hdr200 --distribute=all --exec-policy=serial -r
reframe -c tests/omb-bw-hdr100.py -J reservation="$res" -J constraint=hdr100 --distribute=all --exec-policy=serial -r
reframe -c tests/omb-bw-fdr56.py -J reservation="$res" -J constraint=fdr56 --distribute=all --exec-policy=serial -r
```
