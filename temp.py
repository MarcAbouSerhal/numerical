from typing import Callable, Literal

MAX_SIZE = 16

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

def find_kth(
    l: list,
    k: int
):
    """
    Given a list `l` and an integer `k`, 
    `find_kth` returns `l'[k]` (0-indexed) where `l'` has the elements of `l` sorted in non-decreasing order 
    
    Complexity: O(n) where n is the length of `l`

    Args:
        `l` (`list`):  List whose kth smallest element will be returned
        `k` (`int`): Position in sorted order
    
    Returns:
        `Any`: `l'[k]` (0-indexed) where `l'` has the elements of `l` sorted in non-decreasing order
    """
    while l:
        if k == 0: return min(l)
        n = len(l)
        if k == n - 1: return max(l)
        if n <= MAX_SIZE: return sorted(l)[k]
        pivot = find_kth([sorted(l[i: i + 5])[2] for i in range(0, 5 * (n // 5), 5)], n // 10)
        L = [x for x in L if x < pivot]
        R = [x for x in L if x > pivot]
        for _ in range(sum(1 for x in L if x == pivot)): (L if len(L) < len(R) else R).append(pivot)
        if k < len(L):
            l = L
        else:
            k -= len(L)
            l = R
    return None
