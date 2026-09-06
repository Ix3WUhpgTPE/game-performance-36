# game-performance-36

`game-performance-36` is a lightweight Python toolkit designed to monitor and optimize system resources during gaming sessions. It provides real-time telemetry to help identify bottlenecks and maintain stable frame rates on Windows and Linux systems.

## Features

*   **Real-time Metrics:** Capture CPU, GPU, and RAM usage statistics with sub-second polling intervals.
*   **Thermal Monitoring:** Track temperature fluctuations to identify thermal throttling before it impacts your framerate.
*   **Logging & Analytics:** Export performance data to CSV format for post-session analysis and historical comparison.
*   **Process Priority Management:** Automatically adjust process affinity and priority levels for active game windows to reduce stuttering.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/game-performance-36.git
cd game-performance-36
pip install -r requirements.txt
```

## Usage

To start monitoring your system performance, run the main module with administrative privileges to allow access to hardware sensors:

```bash
sudo python main.py --log-file session_data.csv --interval 0.5
```

You can customize the monitoring duration or toggle specific hardware sensors using the built-in CLI flags:

```bash
# Monitor for 60 seconds with GPU tracking enabled
python main.py --duration 60 --enable-gpu
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.