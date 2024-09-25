import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class mpiGraph_OpenMPI(rfm.RunOnlyRegressionTest):
    descr = "mpiGraph benchmark using gcc/11.3.0 and openmpi/4.1.4 with pmix_v2"
    valid_systems = [
        "discovery:main",
        "discovery:epyc-64",
        "discovery:gpu",
        "discovery:oneweek",
        "endeavour:shared",
        "endeavour:cryoem",
        "endeavour:isi",
        "endeavour:priya",
        "endeavour:qcb",
        "endeavour:scec"
    ]
    valid_prog_environs = [
        "env-gcc-11.3.0-openmpi-4.1.4"
    ]
    sourcesdir = None
    executable = "/project/hpcroot/rfm/resources/mpiGraph/gcc-11.3.0-openmpi-4.1.4/mpiGraph 1048576 10 10"
    num_tasks = 8
    num_tasks_per_node = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "ulimit -s unlimited"
    ]
    env_vars = {
        "SLURM_MPI_TYPE": "pmix_v2",
        "SLURM_CPU_BIND": "verbose"
    }
    reference = {
        "discovery:main": {
            "send_avg": (3000, -0.10, None, "msg_bandwidth"),
            "recv_avg": (3000, -0.10, None, "msg_bandwidth")
        },
        "discovery:epyc-64": {
            "send_avg": (5000, -0.10, None, "msg_bandwidth"),
            "recv_avg": (5000, -0.10, None, "msg_bandwidth")
        },
        "discovery:gpu": {
            "send_avg": (4000, -0.10, None, "msg_bandwidth"),
            "recv_avg": (4000, -0.10, None, "msg_bandwidth")
        },
        "discovery:oneweek": {
            "send_avg": (3000, -0.10, None, "msg_bandwidth"),
            "recv_avg": (3000, -0.10, None, "msg_bandwidth")
        },
        "endeavour:shared": {
            "send_avg": (3700, -0.10, None, "msg_bandwidth"),
            "recv_avg": (3700, -0.10, None, "msg_bandwidth")
        },
        "endeavour:cryoem": {
            "send_avg": (3000, -0.10, None, "msg_bandwidth"),
            "recv_avg": (3000, -0.10, None, "msg_bandwidth")
        },
        "endeavour:isi": {
            "send_avg": (3000, -0.10, None, "msg_bandwidth"),
            "recv_avg": (3000, -0.10, None, "msg_bandwidth")
        },
        "endeavour:priya": {
            "send_avg": (3000, -0.10, None, "msg_bandwidth"),
            "recv_avg": (3000, -0.10, None, "msg_bandwidth")
        },
        "endeavour:qcb": {
            "send_avg": (3000, -0.10, None, "msg_bandwidth"),
            "recv_avg": (3000, -0.10, None, "msg_bandwidth")
        },
        "endeavour:scec": {
            "send_avg": (3000, -0.10, None, "msg_bandwidth"),
            "recv_avg": (3000, -0.10, None, "msg_bandwidth")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"END mpiGraph", self.stdout)

    @performance_function("msg_bandwidth", perf_key = "send_avg")
    def extract_perf_send(self):
        return sn.extractsingle(r"Send avg\s+(?P<S_ret>[0-9]+\.[0-9]+)", self.stdout, "S_ret", float)

    @performance_function("msg_bandwidth", perf_key = "recv_avg")
    def extract_perf_recv(self):
        return sn.extractsingle(r"Recv avg\s+(?P<R_ret>[0-9]+\.[0-9]+)", self.stdout, "R_ret", float)
