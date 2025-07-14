def calculate_ev(odds: int, win_prob: float) -> float:
    if odds > 0:
        payout = odds / 100
    else:
        payout = 100 / abs(odds)
    ev = (win_prob * payout) - (1 - win_prob)
    return round(ev, 2)

def detect_arbitrage(odds_a: float, odds_b: float) -> bool:
    return (1 / odds_a + 1 / odds_b) < 1
