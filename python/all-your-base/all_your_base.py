def rebase(input_base, digits, output_base):
    if output_base <= 1:
        raise ValueError("output base must be greater than 1")
    if input_base <= 1:
        raise ValueError("input base must be greater than 1")
    if len(list(filter(lambda x: x != 0, digits))) == 0:
        return []

    # Build up the value in base 10 first to convert into new base
    base_10_val = 0
    for i in range(len(digits)):
        if digits[i] < 0:
            raise ValueError("digits must all be positive or zero")
        if digits[i] >= input_base:
            raise ValueError("digits must be less than the input base")
        base_10_val += digits[i] * (input_base ** (len(digits) - i - 1))

    new_digits = []
    while base_10_val > 0:
        digit = base_10_val % output_base
        base_10_val = int(base_10_val/output_base)
        new_digits.insert(0, digit)

    return new_digits
    