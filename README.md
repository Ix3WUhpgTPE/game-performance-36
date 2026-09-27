# game-performance-36

`game-performance-36` is a lightweight Python toolkit designed to monitor and optimize system resource allocation for demanding gaming environments. It provides real-time telemetry and automated priority adjustment to ensure maximum framerate stability during intensive CPU and GPU workloads.

### Features
*   **Dynamic Process Prioritization:** Automatically detects active game processes and elevates their CPU scheduling priority.
*   **Thermal Monitoring:** Tracks core temperatures via `psutil` and triggers background tasks to prevent thermal throttling.
*   **Latency Optimizer:** Streamlines system interrupt requests and network buffer settings to reduce input lag in online titles.
*   **One-Click Benchmarking:** Logs frame-time variance and resource consumption into structured CSV reports for easy post-session analysis.

### Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/game-performance-36.git
cd game-performance-36
pip install -r requirements.txt
```

### Usage

To start the background performance monitor and prioritize your currently active game process, run the application with administrative privileges:

```bash
# Run with elevated permissions to allow process priority adjustment
sudo python3 main.py --monitor --optimize
```

You can customize the sensitivity of the performance adjustments by modifying the `config.json` file located in the project root:

```json
{
  "cpu_threshold": 85,
  "refresh_interval": 2.0,
  "auto_optimize": true
}
```

### License
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.