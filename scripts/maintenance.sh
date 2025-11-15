# Launch ReFrame test runs for maintenance periods in multiple tmux sessions
# source scripts/use-reframe.sh
# source scripts/maintenance.sh <res>

# Set reservation name from first argument
export res="$1"

# Run all tests tagged for maintenance once
tmux new-session -d -s rfm-all "reframe -c tests -J reservation=$res -t maintenance -r; bash"

# Run Apptainer tests on all nodes
tmux new-session -d -s rfm-apptainer-hello "reframe -c tests/apptainer-hello.py -J reservation=$res --distribute=all -r; bash"
tmux new-session -d -s rfm-apptainer-gpu-hello "reframe -c tests/apptainer-gpu-hello.py -J reservation=$res --distribute=all -r; bash"

# Run NPB OMP MG test on all nodes
tmux new-session -d -s rfm-npb-omp-mg "reframe -c tests/npb-omp-mg.py -p env-gcc-14.3.0 -J reservation=$res --distribute=all -r; bash"

# Run NPB CUDA LU test on all GPU nodes
tmux new-session -d -s rfm-npb-cuda-lu "reframe -c tests/npb-cuda-lu.py -p env-gcc-14.3.0-cuda-12.9.1 -J reservation=$res --distribute=all -r; bash"

# Run OMB bandwidth and latency tests on all nodes
tmux new-session -d -s rfm-omb-bw "reframe -c tests/omb-bw.py -J reservation=$res --distribute=all -r; bash"
tmux new-session -d -s rfm-omb-latency "reframe -c tests/omb-latency.py -J reservation=$res --distribute=all -r; bash"
