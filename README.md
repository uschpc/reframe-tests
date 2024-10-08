# CARC ReFrame test suite

## Purpose

The CARC [ReFrame](https://reframe-hpc.readthedocs.io/en/stable/index.html) system regression tests for the Discovery and Endeavour clusters are designed to be short-running and to cover broad functionality. The tests include:

- Lmod software modules
- Programming environments (e.g., compilers, toolchains, MPI libraries)
- Parallel programming (e.g., OpenMP, MPI, CUDA)
- Popular applications (e.g., Python, R, Julia)
- Software license server (e.g., MATLAB, Q-Chem)
- I/O on the /home1, /project, /scratch1, and /cryoem2 file systems
- File downloads
- Singularity containers
- Single-node and multi-node jobs

Currently, tests are developed and run using ReFrame v4.6.3.

## License

[0BSD](LICENSE)
