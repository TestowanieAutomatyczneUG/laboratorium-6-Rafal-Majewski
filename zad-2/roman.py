def romanMinus(number: int) -> str:
	for d in [10, 5]:
		if (number + 1) == d:
			return "I"+roman(number+1)

def romanPlus(number: int) -> str:
	if number >= 10:
		return "X"+roman(number-10)
	if number >= 5:
		return "V"+roman(number-5)
	if number == 0:
		return ""
	return roman(number-1) + "I"

def roman(number: int) -> str:
	return romanMinus(number) or romanPlus(number)

if __name__ == "__main__":
	for i in range(0, 20):
		try:
			print(i, roman(i))
		except RecursionError:
			print(i, "RecursionError")

