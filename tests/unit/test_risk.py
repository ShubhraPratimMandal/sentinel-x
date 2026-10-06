from apps.api.app.risk import posture

def test_posture_empty():
    assert posture([]) == 0

def test_posture_bounds():
    assert 0 <= posture([10, 50, 90]) <= 100
