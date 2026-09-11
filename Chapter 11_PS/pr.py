pr = 1 + 10j

# A complex number is not a string, so split() cannot be used directly.
# Store its real and imaginary parts in a list.
parts = [pr.real, pr.imag]

print(parts)  # [1.0, 10.0]