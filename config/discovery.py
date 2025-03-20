# Discovery configuration

site_configuration = {
    "general": [
        {
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "/project2/wjendrze_120/reframe/logs/discovery/reports/run-report-$(date --iso-8601=seconds).json",
        }
    ],
    "systems": [
        {
            "name": "discovery",
            "descr": "Discovery cluster",
            "stagedir": "/project2/wjendrze_120/reframe/logs/discovery/stage/stage-$(date --iso-8601=seconds)",
            "outputdir": "/project2/wjendrze_120/reframe/logs/discovery/output/output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "discovery.*"
            ],
            "partitions": [
                {
                    "name": "allnodes",
                    "descr": "Discovery allnodes partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes"
                    ],
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-gcc-13.3.0-cuda-12.6.3",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl",
                        "env-fio",
                        "env-ior",
                        "env-omb"
                    ]
                },
                {
                    "name": "main",
                    "descr": "Discovery main partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=main"
                    ],
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-hpcg",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl"
                    ]
                },
                {
                    "name": "epyc-64",
                    "descr": "Discovery epyc-64 partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=epyc-64"
                    ],
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-hpcg",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl",
                        "env-fio",
                        "env-ior"
                    ]
                },
                {
                    "name": "gpu",
                    "descr": "Discovery gpu partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=gpu"
                    ],
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-gcc-13.3.0-cuda-12.6.3",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl"
                    ]
                },
                {
                    "name": "largemem",
                    "descr": "Discovery largemem partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=largemem"
                    ],
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl"
                    ]
                },
                {
                    "name": "debug",
                    "descr": "Discovery debug partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=debug"
                    ],
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-gcc-13.3.0-cuda-12.6.3",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl"
                    ]
                },
                {
                    "name": "oneweek",
                    "descr": "Discovery oneweek partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                         "--account=hpcroot",
                         "--partition=oneweek"
                    ],
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-matlab",
                        "env-qchem",
                        "env-curl"
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
                    "name": "/project2/wjendrze_120/reframe/logs/discovery/run/reframe.log",
                    "timestamp": "%FT%T",
                    "format": "[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s",
                    "append": True
                }
            ],
            "handlers_perflog": [
                {
                    "type": "filelog",
                    "level": "info",
                    "basedir": "/project2/wjendrze_120/reframe/logs/discovery/perf",
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
