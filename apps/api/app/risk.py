from .models import Severity

WEIGHTS: dict[Severity, int] = {"LOW": 20, "MEDIUM": 45, "HIGH": 70, "CRITICAL": 90}

def calculate_risk(severity: Severity, confidence: int, indicator_count: int = 1, corroborations: int = 0) -> int:
    base = WEIGHTS[severity]
    confidence_factor = confidence / 100
    corroboration_bonus = min(corroborations * 3, 10)
    indicator_bonus = min(max(indicator_count - 1, 0) * 2, 8)
    return min(100, round(base * (0.7 + 0.3 * confidence_factor) + corroboration_bonus + indicator_bonus),)

def posture(scores: list[int]) -> int:
    if not scores:
        return 0
    return round(sum(scores) / len(scores))
