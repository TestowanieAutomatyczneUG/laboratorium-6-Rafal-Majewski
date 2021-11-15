def roman(number: int) -> str:
	if number >= 4:
		if number == 4:
			return "I"+roman(number+1)
		return "V"+roman(number-5)
	return "I"*number


if __name__ == "__main__":
	for i in range(1, 51):
		print(i, roman(i))