# game-performance-36

`game-performance-36` is a lightweight Python toolkit designed to monitor, analyze, and optimize frame rates and resource utilization for PC gaming environments. It provides real-time telemetry and automated system adjustment scripts to ensure peak performance during intense gameplay sessions.

## Features

*   **Real-time Telemetry:** Captures CPU/GPU temperature, load percentages, and frame time variance with sub-millisecond latency.
*   **Process Priority Orchestrator:** Automatically assigns high-priority CPU affinity to target game executables while background tasks are throttled.
*   **Thermal Throttling Mitigation:** Dynamically adjusts system power profiles when hardware temperature thresholds are breached to prevent stuttering.
*   **Performance Benchmarking:** Exports high-fidelity session logs to CSV for deep-dive analysis in Excel or pandas.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/game-performance-36.git
cd game-performance-36
pip install -r requirements.txt
```

*Note: Administrative/Sudo privileges are required for process priority management.*

## Basic Usage

To monitor a specific application during gameplay, run the main module with the process name:

```bash
python monitor.py --process "eldenring.exe" --interval 0.5
```

For a full optimization run that applies settings automatically:

```bash
python optimizer.py --mode aggressive --target "cyberpunk2077.exe"
```

The tool will output performance snapshots directly to the console and generate a `session_log.csv` upon exit.

## Contributing
Contributions are welcome. Please open an issue to discuss proposed enhancements before submitting a pull request.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.