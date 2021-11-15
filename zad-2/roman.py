def romanMinus(number: int) -> str:
	for d in [10, 5]:
		if (number + 1) % d == 0:
			return "I"+roman(number+1)

def roman(number: int) -> str:
	if number == 0:
		return ""
	if number == 5:
		return "V"
	if number == 10:
		return "X"
	return romanMinus(number) or roman(number-1) + "I"

if __name__ == "__main__":
	for i in range(0, 20):
		try:
			print(i, roman(i))
		except RecursionError:
			print(i, "RecursionError")