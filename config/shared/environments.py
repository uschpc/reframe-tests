# Environments configuration

site_configuration = {
    "environments": [
        {
             "name": "env-none",
             "modules": [
             ]
        },
        {
             "name": "env-apptainer",
             "modules": [
                 "apptainer/1.4.5"
             ]
        },
        {
            "name": "env-gcc-14.3.0",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "gmake/4.4.1"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-14.3.0-cuda-12.9.1",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "gmake/4.4.1",
                "cuda/12.9.1"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-14.3.0-mpich-4.3.1",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "gmake/4.4.1",
                "mpich/4.3.1"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
        },
        {
            "name": "env-gcc-14.3.0-openmpi-5.0.8",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "gmake/4.4.1",
                "openmpi/5.0.8"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
        },
        {
            "name": "env-gcc-13.3.0",
            "modules": [
                "gcc/13.3.0",
                "gmake/4.4.1"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-13.3.0-cuda-12.6.3",
            "modules": [
                "gcc/13.3.0",
                "gmake/4.4.1",
                "cuda/12.6.3"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-13.3.0-mpich-4.2.2",
            "modules": [
                "gcc/13.3.0",
                "gmake/4.4.1",
                "mpich/4.2.2"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
        },
        {
            "name": "env-gcc-13.3.0-openmpi-5.0.5",
            "modules": [
                "gcc/13.3.0",
                "gmake/4.4.1",
                "openmpi/5.0.5"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
        },
        {
            "name": "env-hpcg",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "mpich/4.3.1",
                "hpcg/3.1"
            ]
        },
        {
            "name": "env-omb",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "mpich/4.3.1",
                "osu-micro-benchmarks/7.5.1"
            ]
        },
        {
            "name": "env-fio",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "fio/3.41"
            ]
        },
        {
            "name": "env-ior",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "mpich/4.3.1",
                "ior/3.3.0"
            ]
        },
        {
            "name": "env-git",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "git/2.51.0"
            ]
        },
        {
            "name": "env-julia",
            "modules": [
                "julia/1.12.4"
            ]
        },
        {
            "name": "env-python",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "python/3.11.13"
            ]
        },
        {
            "name": "env-r",
            "modules": [
                "rstats/4.5.2"
            ]
        },
        {
            "name": "env-matlab",
            "modules": [
                "matlab/2024a"
            ]
        },
        {
            "name": "env-qchem",
            "modules": [
                "qchem/6.3.0-openmp"
            ]
        }
    ]
}
