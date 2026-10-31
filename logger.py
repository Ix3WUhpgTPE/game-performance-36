import logging
import os
from logging.handlers import RotatingFileHandler


class PerformanceLogFormatter(logging.Formatter):
    """Custom formatter tagging frame latency and dynamic severity."""

    def format(self, record):
        fps = getattr(record, "fps", None)
        if fps is not None:
            if fps < 30:
                record.levelname = "CRITICAL_FPS"
            elif fps < 60:
                record.levelname = "LOW_FPS"
        frame_time = getattr(record, "frame_ms", 0.0)
        record.perf_tag = f"[FPS:{fps if fps else 'N/A'}|{frame_time:.1f}ms]"
        return super().format(record)


def setup_game_logger(
    log_dir: str = "logs", max_bytes: int = 1_048_576, backup_count: int = 5
) -> logging.Logger:
    """Configures a gaming performance logger with dynamic size rotation."""
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "frame_metrics.log")

    logger = logging.getLogger("GamePerformance")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )

    fmt = "%(asctime)s %(perf_tag)s [%(levelname)s] %(message)s"
    formatter = PerformanceLogFormatter(fmt=fmt, datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def log_frame(logger: logging.Logger, frame_id: int, fps: float, frame_ms: float) -> None:
    """Helper to emit frame performance logs with extra context."""
    extra = {"fps": fps, "frame_ms": frame_ms}
    if fps < 30:
        logger.warning(
            f"Frame #{frame_id} rendered slow, dynamic downgrade suggested",
            extra=extra,
        )
    else:
        logger.debug(f"Frame #{frame_id} rendered smoothly", extra=extra)
