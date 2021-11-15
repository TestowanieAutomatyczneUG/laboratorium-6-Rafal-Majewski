def romanMinus(number: int) -> str:
	for d in [10, 5]:
		if (number + 1) % d == 0:
			return "I"+roman(number+1)

def roman(number: int) -> str:
	if number == 0:
		return ""
	if number == 5:
		return "V"
	return romanMinus(number) or roman(number-1) + "I"

