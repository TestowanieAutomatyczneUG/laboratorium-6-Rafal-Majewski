def roman(number: int) -> str:
	if number >= 4:
		return "IV"+roman(number-4)
	return "I"*number
