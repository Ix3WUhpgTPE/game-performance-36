# game-performance-36

`game-performance-36` is a lightweight Python toolkit designed to monitor and optimize system resources during gaming sessions. It provides real-time telemetry to help developers and power users identify performance bottlenecks and frame-time inconsistencies.

## Features

*   **Real-time Metrics:** Capture live CPU, GPU, and RAM utilization data with millisecond precision.
*   **Frame-Time Analysis:** Automated logging of frame delivery consistency to detect micro-stuttering issues.
*   **Process Priority Injection:** Dynamic adjustment of Windows/Linux process priority to minimize background interference.
*   **Hardware Snapshot:** Exports comprehensive system state reports in JSON format for easy post-session benchmarking.

## Installation

Ensure you have Python 3.8+ installed on your system. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/game-performance-36.git
cd game-performance-36
pip install -r requirements.txt
```

## Usage

To monitor a specific game process by its PID, run the following command:

```bash
python monitor.py --pid 1234 --log-output session_data.json
```

For a comprehensive system-wide performance scan without locking to a single process:

```bash
python monitor.py --global --duration 60
```

The tool will output an interactive console dashboard and save the finalized metrics to your working directory once the monitoring window closes.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.