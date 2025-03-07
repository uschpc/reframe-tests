# Laguna configuration

site_configuration = {
    "general": [
        {
            "check_search_path": [
                "tests/"
            ],
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "/project/jkhong_1307/rfm/reports/laguna-run-report-$(date --iso-8601=seconds).json",
        }
    ],
    "systems": [
        {
            "name": "laguna",
            "descr": "Laguna regional cluster",
            "stagedir": "/project/jkhong_1307/rfm/stage/laguna-stage-$(date --iso-8601=seconds)",
            "outputdir": "/project/jkhong_1307/rfm/output/laguna-output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "laguna1.carc.usc.edu"
            ],
            "partitions": [
                {
                    "name": "compute",
                    "descr": "Laguna compute partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=jkhong_1307",
                        "--partition=compute"
                    ],
                    "max_jobs": 100,
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-gcc-13.3.0-mpich-4.2.2",
                        "env-hpcg",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-curl",
                        "env-fio",
                        "env-ior"
                    ]
                },
                {
                    "name": "gpu",
                    "descr": "Laguna gpu partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=jkhong_1307",
                        "--partition=gpu"
                    ],
                    "max_jobs": 100,
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
                    "name": "./logs/reframe-laguna.log",
                    "timestamp": "%FT%T",
                    "format": "[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s",
                    "append": True
                }
            ],
            "handlers_perflog": [
                {
                    "type": "filelog",
                    "level": "info",
                    "basedir": "./perflogs",
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
