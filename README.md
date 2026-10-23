# game-performance-36

`game-performance-36` is a lightweight Python toolkit designed to monitor and optimize system resource allocation for high-performance gaming. It identifies bottlenecks in CPU scheduling and memory throughput to ensure stable frame rates during intensive sessions.

## Features

*   **Real-time Telemetry:** Tracks CPU core utilization and GPU temperature trends with sub-second polling rates.
*   **Process Prioritization:** Automatically elevates the priority of active game executables to minimize input latency.
*   **Background Bloat Suppression:** Temporarily suspends resource-heavy non-gaming processes to free up RAM.
*   **Hardware-Aware Profiling:** Generates optimized configuration reports based on your specific GPU/CPU architecture.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the dependencies:

```bash
git clone https://github.com/Developer/game-performance-36.git
cd game-performance-36
pip install -r requirements.txt
```

## Usage

To start the monitoring engine and apply default optimizations, run the script with elevated privileges:

```bash
# Run with administrative/sudo permissions for process management
sudo python main.py --mode optimize --target "game_executable_name"
```

You can also run the monitor in background mode to log performance data to a CSV file:

```bash
python main.py --log --output ./logs/session_01.csv
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.