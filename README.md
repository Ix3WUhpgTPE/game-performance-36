# game-performance-36

`game-performance-36` is a lightweight Python toolkit designed to monitor and optimize system resource allocation for high-demand gaming sessions. It provides real-time telemetry to help developers and power users identify bottlenecking processes and thermal throttling issues.

## Features

*   **Real-time Metrics:** Tracks CPU/GPU utilization, RAM frequency, and frame-time consistency with sub-second polling rates.
*   **Process Affinity Tuning:** Automatically assigns high-priority execution threads to gaming processes to minimize stuttering.
*   **Thermal Guard:** Triggers automated warnings or custom scripts when GPU junction temperatures exceed defined safety thresholds.
*   **Performance Profiling:** Exports session data into structured CSV logs for comparative analysis of hardware configurations.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/game-performance-36.git
cd game-performance-36
pip install -r requirements.txt
```

*Note: Administrative/Sudo privileges are required to modify process affinity settings.*

## Usage

To start the monitor in background mode with default settings, run the following command:

```bash
python main.py --monitor --log-level=INFO
```

You can specify a target process name to isolate performance data:

```bash
python main.py --target "eldenring.exe" --threshold 85
```

For a full list of configuration parameters, run:

```bash
python main.py --help
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.