import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class FileDownload(rfm.RunOnlyRegressionTest):
    descr = "File download"
    valid_systems = [
        "pathfinder:compute",
        "pathfinder:gpu"
    ]
    valid_prog_environs = [
        "env-curl"
    ]
    sourcesdir = None
    executable = "curl -L https://www.carc.usc.edu/index.html"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"USC Center for Advanced Research Computing", self.stdout)
