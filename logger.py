import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


class FPSAwareFormatter(logging.Formatter):
    """Custom log formatter injecting FPS state and latency tags into game telemetry."""

    def format(self, record: logging.LogRecord) -> str:
        fps = getattr(record, "fps", 60.0)
        frame_time = getattr(record, "frame_time_ms", 16.67)

        if fps < 30.0:
            status = "CRITICAL_DROP"
        elif fps < 55.0:
            status = "STUTTER"
        else:
            status = "SMOOTH"

        record.perf_tag = f"[{status} | {fps:.1f} FPS | {frame_time:.2f}ms]"
        return super().format(record)


class TelemetryRotatingHandler(RotatingFileHandler):
    """Rotating file handler capable of epoch-based triggers during performance dips."""

    def __init__(self, filename: str, max_bytes: int = 2_097_152, backup_count: int = 5):
        super().__init__(filename, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8")

    def emit_with_frame_context(self, record: logging.LogRecord, force_rotation: bool = False) -> None:
        if force_rotation and self.stream:
            self.doRollover()
        self.emit(record)


def setup_game_logger(
    logger_name: str = "game_perf",
    log_file: str = "logs/telemetry.log",
    max_megabytes: int = 5,
    backup_count: int = 4,
    log_level: int = logging.INFO
) -> logging.Logger:
    """Configures a rotating logger tuned for real-time gaming performance output."""
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.propagate = False

    if logger.handlers:
        logger.handlers.clear()

    log_dir = os.path.dirname(os.path.abspath(log_file))
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    handler = TelemetryRotatingHandler(
        filename=log_file,
        max_bytes=max_megabytes * 1024 * 1024,
        backup_count=backup_count
    )

    format_pattern = "%(asctime)s %(perf_tag)s [%(levelname)s] %(message)s"
    handler.setFormatter(FPSAwareFormatter(format_pattern, datefmt="%H:%M:%S"))

    logger.addHandler(handler)
    return logger
