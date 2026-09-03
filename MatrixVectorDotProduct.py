# ============================================================
# Matrix-Vector Dot Product
# ============================================================
#
# Linear Algebra
#
# Problem:
# Write a Python function that computes the dot product of a
# matrix and a vector.
#
# The operation is valid only when the number of columns in
# the matrix is equal to the length of the vector.
#
# For an n × m matrix, the vector must have a length of m.
#
# The function should:
#   - Return the resulting vector if the dimensions are valid.
#   - Return -1 if the dimensions are incompatible.
#
# Example:
#
# Input:
#     a = [[1, 2],
#          [2, 4]]
#
#     b = [1, 2]
#
# Output:
#     [5, 10]
#
# Reasoning:
#
# Row 1:
#     (1 × 1) + (2 × 2) = 1 + 4 = 5
#
# Row 2:
#     (2 × 1) + (4 × 2) = 2 + 8 = 10
#
# Therefore:
#     result = [5, 10]
#
# Key idea:
# Each output element is the dot product between one row of
# the matrix and the entire vector.
#
# Matrix:
#     [[1, 2],
#      [2, 4]]
#
# Vector:
#     [1, 2]
#
# Dimension requirement:
#     number of columns in matrix == length of vector
#
# ============================================================





def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	if len(a[0]) != len(b):
		return -1
	
	result = []

	for row in a:
		total = 0

		for i in range(len(b)):
			total += row[i] * b[i]

		result.append(total)



	return result