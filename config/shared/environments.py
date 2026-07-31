# Environments configuration

site_configuration = {
    "environments": [
        {
             "name": "none",
             "modules": [
             ]
        },
        {
             "name": "apptainer-1.5.3",
             "modules": [
                 "apptainer/1.5.3"
             ]
        },
        {
             "name": "apptainer-1.4.5",
             "modules": [
                 "apptainer/1.4.5"
             ]
        },
        {
             "name": "apptainer-1.3.6",
             "modules": [
                 "apptainer/1.3.6"
             ]
        },
        {
            "name": "gcc-15.3.0",
            "modules": [
                "ver/2607",
                "gcc/15.3.0",
                "gmake/4.4.1"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "gcc-15.3.0-cuda-13.0.3",
            "modules": [
                "ver/2607",
                "gcc/15.3.0",
                "gmake/4.4.1",
                "cuda/13.0.3"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "gcc-15.3.0-mpich-5.0.1",
            "modules": [
                "ver/2607",
                "gcc/15.3.0",
                "gmake/4.4.1",
                "mpich/5.0.1"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
        },
        {
            "name": "gcc-14.3.0",
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
            "name": "gcc-14.3.0-cuda-12.9.1",
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
            "name": "gcc-14.3.0-mpich-4.3.1",
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
            "name": "gcc-14.3.0-openmpi-5.0.8",
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
            "name": "gcc-13.3.0",
            "modules": [
                "gcc/13.3.0",
                "gmake/4.4.1"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "gcc-13.3.0-cuda-12.6.3",
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
            "name": "gcc-13.3.0-mpich-4.2.2",
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
            "name": "gcc-13.3.0-openmpi-5.0.5",
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
            "name": "hpcg",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "mpich/4.3.1",
                "hpcg/3.1"
            ]
        },
        {
            "name": "omb",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "mpich/4.3.1",
                "osu-micro-benchmarks/7.5.1"
            ]
        },
        {
            "name": "fio",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "fio/3.41"
            ]
        },
        {
            "name": "ior",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "mpich/4.3.1",
                "ior/3.3.0"
            ]
        },
        {
            "name": "git",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "git/2.51.0"
            ]
        },
        {
            "name": "julia-1.12.6",
            "modules": [
                "julia/1.12.6"
            ]
        },
        {
            "name": "julia-1.11.9",
            "modules": [
                "julia/1.11.9"
            ]
        },
        {
            "name": "julia-1.10.11",
            "modules": [
                "julia/1.10.11"
            ]
        },
        {
            "name": "python",
            "modules": [
                "ver/2506",
                "gcc/14.3.0",
                "python/3.13.11"
            ]
        },
        {
            "name": "r-4.6.1",
            "modules": [
                "r/4.6.1"
            ]
        },
        {
            "name": "r-4.5.3",
            "modules": [
                "r/4.5.3"
            ]
        },
        {
            "name": "r-4.4.3",
            "modules": [
                "r/4.4.3"
            ]
        },
        {
            "name": "matlab",
            "modules": [
                "matlab/2025b"
            ]
        },
        {
            "name": "qchem",
            "modules": [
                "qchem/6.4.0"
            ]
        }
    ]
}
