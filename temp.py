from typing import Callable, Literal

def find_tail(
    f: Callable[[float], Literal[0, 1]],
    l: float,
    delta: float = 1e-6
) -> float:
    """
    Given a real number `delta` (`10⁻⁶` if not specified), a function `f: ℝ⁺ → {0,1}` and a real number `l > 0` where 
    there exists `x₀ ≥ l` such that `f(x) = 0` `∀x < x₀` and `f(x) = 1` `∀x > x₀`,
    `find_tail` returns a real number `x₀'` such that `|x₀' - x₀| ≤ delta`

    Args:
        `f` (`Callable[[float], int]`): Function whose approximate tail `x₀'` will be calculated
        `l` (`float`): Lower bound for `x₀`
        `delta` (`float`, optional): Maximum absolute difference between real and approximate values

    Returns:
        `float`: A real number `x₀'` such that `|x₀' - x₀| ≤ delta`
    """
    x_high = 2 * l
    while f(x_high) == 0: x_high *= 2
    x_low = x_high / 2
    while x_high - x_low > delta:
        x_mid = (x_low + x_high) / 2
        if f(x_mid) == 1: x_high = x_mid
        else: x_low = x_mid
    return x_high
