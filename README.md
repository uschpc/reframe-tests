# CARC ReFrame test suite

## Purpose

The CARC [ReFrame](https://reframe-hpc.readthedocs.io/en/stable/index.html) system regression tests are designed to be short-running and to cover broad functionality. The tests include:

- Software modules
- Programming environments (compilers, toolchains, MPI libraries, etc.)
- Parallel programming (OpenMP, MPI, CUDA)
- Popular applications (Python, R, etc.)
- Single-node and multi-node jobs
- License server (e.g., Matlab, Q-Chem)
- I/O on the /home1, /project, /scratch1, and /scratch2 file systems
- File downloads
- Singularity containers

Currently, tests are developed and run using ReFrame v4.4.2.

## License

[0BSD](LICENSE)
