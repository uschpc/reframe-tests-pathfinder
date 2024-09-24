# Pathfinder configuration

site_configuration = {
    "general": [
        {
            "check_search_path": [
                "tests/"
            ],
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "/home/hpcroot/rfm/reports/pathfinder-run-report-$(date --iso-8601=seconds).json",
        }
    ],
    "systems": [
        {
            "name": "pathfinder",
            "descr": "Pathfinder testbed cluster",
            "stagedir": "/home/hpcroot/rfm/stage/pathfinder-stage-$(date --iso-8601=seconds)",
            "outputdir": "/home/hpcroot/rfm/output/pathfinder-output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "wolf-test"
            ],
            "partitions": [
                {
                    "name": "compute",
                    "descr": "Pathfinder compute partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=wjendrze_1",
                        "--partition=compute"
                    ],
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-mpigraph",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-curl",
                        "env-fio"
                    ]
                },
                {
                    "name": "gpu",
                    "descr": "Pathfinder gpu partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=wjendrze_1",
                        "--partition=gpu"
                    ],
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-cuda-12.4.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-mpigraph",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-curl",
                        "env-fio"
                    ]
                }
            ]
        }
    ],
    "environments": [
        {
             "name": "env-apptainer",
             "modules": [
                 "apptainer/1.3.3"
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
            "name": "env-gcc-13.3.0-cuda-12.4.0",
            "modules": [
                "gcc/13.3.0",
                "cuda/12.4.0"
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
            "ftn": "mpif90"
        },
        {
            "name": "env-mpigraph",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "mpigraph/main"
            ]
        },
        {
            "name": "env-julia",
            "modules": [
                "julia/1.10.5"
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
                "openblas/0.3.28",
                "r/4.4.1"
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
                "fio/3.37"
            ]
        }
    ],
    "logging": [
        {
            "handlers": [
                {
                    "type": "file",
                    "level": "debug",
                    "name": "./logs/reframe-pathfinder.log",
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
