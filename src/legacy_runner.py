"""Legacy checkpoint runner for the Quasar Flow 1.5 line."""

from __future__ import annotations


def restore(payload: bytes, expected_size: int) -> bytes:
    if expected_size <= 0:
        raise ValueError("expected_size must be positive")
    if len(payload) % expected_size != 0:
        raise ValueError("payload does not divide evenly into the checkpoint frame")
    return payload


def frame_count(payload: bytes, frame_size: int) -> int:
    if frame_size <= 0:
        raise ValueError("frame_size must be positive")
    return len(payload) // frame_size
