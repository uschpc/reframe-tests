# Environments configuration

site_configuration = {
    "environments": [
        {
             "name": "env-apptainer",
             "modules": [
                 "apptainer/1.3.6"
             ]
        },
        {
            "name": "env-gcc-13.3.0",
            "modules": [
                "gcc/13.3.0"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-13.3.0-cuda-12.6.3",
            "modules": [
                "gcc/13.3.0",
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
                "openmpi/5.0.5"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90",
            "env_vars": [
                ["SLURM_MPI_TYPE", "pmix_v5"]
            ]
        },
        {
            "name": "env-gcc-13.3.0-mpich-4.2.2",
            "modules": [
                "gcc/13.3.0",
                "mpich/4.2.2"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90",
            "env_vars": [
                ["SLURM_MPI_TYPE", "pmi2"]
            ]
        },
        {
            "name": "env-hpcg",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "hpcg/3.1"
            ],
            "env_vars": [
                ["SLURM_MPI_TYPE", "pmix_v5"]
            ]
        },
        {
            "name": "env-julia",
            "modules": [
                "julia/1.11.3"
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
                "gcc/13.3.0",
                "r/4.4.2"
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
                "qchem/6.2.0"
            ]
        },
        {
            "name": "env-curl",
            "modules": [
                "gcc/13.3.0",
                "curl/8.8.0"
            ]
        },
        {
            "name": "env-fio",
            "modules": [
                "gcc/13.3.0",
                "fio/3.37",
            ]
        },
        {
            "name": "env-ior",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "ior/3.3.0"
            ],
            "env_vars": [
                ["SLURM_MPI_TYPE", "pmix_v5"]
            ]
        }
    ]
}
