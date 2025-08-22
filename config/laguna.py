# Laguna configuration

site_configuration = {
    "general": [
        {
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "logs/laguna/reports/run-report-$(date --iso-8601=seconds).json"
        }
    ],
    "systems": [
        {
            "name": "laguna",
            "descr": "Laguna regional cluster",
            "stagedir": "logs/laguna/stage/stage-$(date --iso-8601=seconds)",
            "outputdir": "logs/laguna/output/output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "laguna1.carc.usc.edu"
            ],
            "partitions": [
                {
                    "name": "login",
                    "descr": "Laguna login node",
                    "scheduler": "local",
                    "launcher": "local",
                    "max_jobs": 5,
                    "environs": [
                        "env-none"
                    ]
                },
                {
                    "name": "allnodes",
                    "descr": "Laguna allnodes partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes"
                    ],
                    "max_jobs": 1000,
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-gcc-13.3.0-cuda-12.6.3",
                        "env-hpcg",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-git",
                        "env-fio",
                        "env-omb"
                    ]
                },
                {
                    "name": "compute",
                    "descr": "Laguna compute partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=compute"
                    ],
                    "max_jobs": 1000,
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-hpcg",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-git",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "gpu",
                    "descr": "Laguna gpu partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=gpu"
                    ],
                    "max_jobs": 1000,
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-gcc-13.3.0-cuda-12.6.3",
                        "env-hpcg",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-git",
                        "env-fio",
                        "env-omb"
                    ]
                }
            ]
        }
    ],
    "logging": [
        {
            "handlers": [
                {
                    "type": "file",
                    "level": "debug",
                    "name": "logs/laguna/run/reframe.log",
                    "timestamp": "%FT%T",
                    "format": "[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s",
                    "append": True
                }
            ],
            "handlers_perflog": [
                {
                    "type": "filelog",
                    "level": "info",
                    "basedir": "logs/laguna/perf",
                    "prefix": "%(check_system)s/%(check_partition)s",
                    "format": (
                        "%(check_job_completion_time)s,%(version)s,"
                        "%(check_display_name)s,%(check_system)s,"
                        "%(check_partition)s,%(check_environ)s,"
                        "%(check_jobid)s,%(check_result)s,%(check_perfvalues)s"
                    ),
                    "format_perfvars": (
                        "%(check_perf_value)s,%(check_perf_unit)s,"
                        "%(check_perf_ref)s,%(check_perf_lower_thres)s,"
                        "%(check_perf_upper_thres)s,"
                    ),
                    "datefmt": "%FT%T",
                    "append": True
                }
            ]
        }
    ]
}
