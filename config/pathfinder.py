# Pathfinder configuration

site_configuration = {
    "general": [
        {
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "logs/pathfinder/reports/run-report-$(date --iso-8601=seconds).json"
        }
    ],
    "systems": [
        {
            "name": "pathfinder",
            "descr": "Pathfinder cluster",
            "stagedir": "logs/pathfinder/stage/stage-$(date --iso-8601=seconds)",
            "outputdir": "logs/pathfinder/output/output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "wolf-test"
            ],
            "partitions": [
                {
                    "name": "login",
                    "descr": "Pathfinder login node",
                    "scheduler": "local",
                    "launcher": "local",
                    "max_jobs": 5,
                    "environs": [
                        "env-none"
                    ]
                },
                {
                    "name": "allnodes",
                    "descr": "Pathfinder allnodes partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes"
                    ],
                    "max_jobs": 1000,
                    "environs": [
                        "env-none",
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-git",
                        "env-fio"
                    ]
                },
                {
                    "name": "xeon-2640v3",
                    "descr": "Pathfinder xeon-2640v3 nodes",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=hpcroot",
                        "--partition=allnodes",
                        "--constraint=xeon-2640v3"
                    ],
                    "max_jobs": 1000,
                    "environs": [
                        "env-none",
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-git",
                        "env-fio"
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
                    "name": "logs/pathfinder/run/reframe.log",
                    "timestamp": "%FT%T",
                    "format": "[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s",
                    "append": True
                }
            ],
            "handlers_perflog": [
                {
                    "type": "filelog",
                    "level": "info",
                    "basedir": "logs/pathfinder/perf",
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
