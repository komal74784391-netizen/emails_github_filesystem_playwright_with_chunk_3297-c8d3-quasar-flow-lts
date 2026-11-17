from src.legacy_runner import frame_count, restore


def test_restore_accepts_aligned_payload():
    assert restore(b"abcd", 2) == b"abcd"


def test_frame_count():
    assert frame_count(b"abcdef", 3) == 2
