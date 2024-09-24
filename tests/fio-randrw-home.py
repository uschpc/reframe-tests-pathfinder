import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class FioRandrwHome(rfm.RunOnlyRegressionTest):
    descr = "Fio random read/write benchmark for /home file system"
    valid_systems = [
        "pathfinder:compute",
        "pathfinder:gpu"
    ]
    valid_prog_environs = [
        "env-fio"
    ]
    sourcesdir = "./src/fio-randrw"
    executable = "bash fio-randrw-home.sh"
    num_tasks = 1
    num_cpus_per_task = 4
    time_limit = "5m"
    reference = {
        "pathfinder:compute": {
            "avg_write_speed": (33.0, -0.1, None, "MiB/sec"),
            "avg_read_speed": (33.0, -0.1, None, "MiB/sec")
        },
        "pathfinder:gpu": {
            "avg_write_speed": (49.0, -0.1, None, "MiB/sec"),
            "avg_read_speed": (49.0, -0.1, None, "MiB/sec")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"all jobs", self.stdout)

    @performance_function("MiB/sec", perf_key = "avg_write_speed")
    def extract_perf_write(self):
        return sn.extractsingle(r"WRITE:\sbw=(?P<W_ret>\d+.\d+)", self.stdout, "W_ret", float)

    @performance_function("MiB/sec", perf_key = "avg_read_speed")
    def extract_perf_read(self):
        return sn.extractsingle(r"READ:\sbw=(?P<R_ret>\d+.\d+)", self.stdout, "R_ret", float)
