# game-performance-36

`game-performance-36` is a lightweight Python toolkit designed to monitor, analyze, and optimize system resource allocation for high-demand PC gaming sessions. It provides real-time telemetry to help developers and power users identify performance bottlenecks and frame-rate stutters.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Key Features

*   **Process Priority Management:** Automatically elevates your game process priority to ensure CPU thread scheduling favors the gaming engine.
*   **Thermal Throttling Detection:** Tracks CPU and GPU temperature spikes, logging performance degradation events to a CSV file for post-session review.
*   **Background Bloat Cleaner:** Automatically suspends non-essential background processes and high-latency browser tabs while a detected game window is active.
*   **Frame-Time Logging:** Hooks into system monitors to calculate precise frame-time consistency and millisecond-latency drift.

## Installation

Ensure you have Python 3.8+ installed. It is recommended to use a virtual environment:

```bash
# Clone the repository
git clone https://github.com/Developer/game-performance-36.git
cd game-performance-36

# Install required dependencies
pip install -r requirements.txt
```

## Basic Usage

Run the monitor as an administrator to ensure the script has the necessary permissions to adjust process priority and suspend background tasks.

```bash
# Start monitoring the active window
python main.py --monitor --process-name "eldenring.exe"
```

To enable the automatic cleanup mode that kills idle background tasks during gameplay, use the `--optimize` flag:

```bash
python main.py --monitor --optimize --log-path ./logs/session_01.csv
```

## Configuration

Settings such as process sensitivity, background task whitelist, and temperature thresholds can be modified in the `config.yaml` file located in the root directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.