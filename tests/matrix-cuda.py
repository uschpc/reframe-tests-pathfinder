import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class MatrixCUDA(rfm.RegressionTest):
    descr = "Matrix-vector multiplication example using CUDA with GPU"
    valid_systems = [
        "pathfinder:gpu"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-cuda-12.4.0"
    ]
    sourcesdir = "./src/matrix-cuda"
    sourcepath = "matrix-vector-multiplication-cuda.cu"
    build_system = "SingleSource"
    executable_opts = [
        "10000",
        "10000"
    ]
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    reference = {
        "*": {
            "gflops": (43.9, -0.1, None, "gflops")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--gpus-per-task=1"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Gflop/s", self.stdout)

    @performance_function("gflops", perf_key = "gflops")
    def extract_perf(self):
        return sn.extractsingle(r"Performance:\s(?P<gflops_ret>[0-9]+.[0-9]+)", self.stdout, "gflops_ret", float)
