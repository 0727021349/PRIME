def calculator_add(n):
	if not isinstance(n, int):
		return "Only integers allowed"
	if n == 1:
		return 1
	elif n <= 0:
		return 0
	return n + calculator_add(n-1)

print calculator_add(100)
