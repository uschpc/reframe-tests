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
                        "none"
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
                        "none",
                        "apptainer",
                        "gcc-14.3.0",
                        "gcc-14.3.0-mpich-4.3.1",
                        "gcc-14.3.0-openmpi-5.0.8",
                        "gcc-13.3.0",
                        "gcc-13.3.0-mpich-4.2.2",
                        "gcc-13.3.0-openmpi-5.0.5",
                        "fio",
                        "git",
                        "julia",
                        "python",
                        "r"
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
                        "none",
                        "apptainer",
                        "gcc-14.3.0",
                        "gcc-14.3.0-mpich-4.3.1",
                        "gcc-14.3.0-openmpi-5.0.8",
                        "gcc-13.3.0",
                        "gcc-13.3.0-mpich-4.2.2",
                        "gcc-13.3.0-openmpi-5.0.5",
                        "fio",
                        "git",
                        "julia",
                        "python",
                        "r"
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
