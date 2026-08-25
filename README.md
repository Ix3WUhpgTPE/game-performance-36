# game-performance-36

game-performance-36 is a Python library that helps game developers monitor and optimize the performance of their titles. It tracks key metrics like frame times, CPU load, and memory consumption in real time, allowing for quick identification of optimization opportunities.

## Features
- Precise frame time profiling with support for custom game loop phases
- Real-time alerts for performance regressions during development
- Built-in exporters for JSON, CSV, and visual reports
- Seamless integration with Pygame and other Python game frameworks

## Installation

```bash
pip install game-performance-36
```

For the latest development version:

```bash
git clone https://github.com/developer/game-performance-36.git
cd game-performance-36
pip install -e .
```

## Usage

```python
from game_performance_36 import PerformanceProfiler

profiler = PerformanceProfiler()

while running:
    profiler.start_frame()
    update_game()
    render_game()
    profiler.end_frame()

    if profiler.should_report():
        profiler.save_report("performance.json")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)