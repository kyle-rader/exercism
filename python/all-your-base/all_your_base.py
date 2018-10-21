from typing import List


def rebase(input_base: int, digits: List[int], output_base: int) -> List[int]:
    if output_base <= 1 or input_base <= 1:
        raise ValueError("bases must be greater than 1")
    if not all(input_base > d >= 0 for d in digits):
        raise ValueError("All digits must be greater than or equal to zero and less than the input base")
    if not any(digits):
        return []

    # Build up the value in base 10 first to convert into new base
    base_10_val = 0
    for i in range(len(digits)):
        base_10_val += digits[i] * (input_base ** (len(digits) - i - 1))

    new_digits = []
    while base_10_val > 0:
        digit = base_10_val % output_base
        base_10_val = int(base_10_val/output_base)
        new_digits.insert(0, digit)

    return new_digits
