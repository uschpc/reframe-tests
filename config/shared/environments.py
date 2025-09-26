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
                 "apptainer/1.4.2"
             ]
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
            "name": "env-hpcg",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "hpcg/3.1"
            ]
        },
        {
            "name": "env-omb",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "osu-micro-benchmarks/7.5"
            ]
        },
        {
            "name": "env-julia",
            "modules": [
                "julia/1.11.7"
            ]
        },
        {
            "name": "env-python",
            "modules": [
                "gcc/13.3.0",
                "python/3.11.9"
            ]
        },
        {
            "name": "env-r",
            "modules": [
                "rstats/4.5.1"
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
        },
        {
            "name": "env-git",
            "modules": [
                "gcc/13.3.0",
                "git/2.45.2"
            ]
        },
        {
            "name": "env-fio",
            "modules": [
                "gcc/13.3.0",
                "fio/3.37"
            ]
        },
        {
            "name": "env-ior",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "ior/3.3.0"
            ]
        }
    ]
}
