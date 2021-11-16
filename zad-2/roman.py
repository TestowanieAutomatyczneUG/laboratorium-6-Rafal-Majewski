def roman(number: int) -> str:
	valuesAndSymbols = [
		(1000, "M"),
		(900, "CM"),
		(500, "D"),
		(400, "CD"),
		(100, "C"),
		(90, "XC"),
		(50, "L"),
		(40, "XL"),
		(10, "X"),
		(9, "IX"),
		(5, "V"),
		(4, "IV"),
		(1, "I")
	]
	result = ""
	for value, symbol in valuesAndSymbols:
		while number >= value:
			result += symbol
			number -= value
	return result


