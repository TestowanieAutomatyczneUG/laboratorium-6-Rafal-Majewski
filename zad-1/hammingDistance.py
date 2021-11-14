def hammingDistance(text1, text2):
	if len(text1) != len(text2):
		raise ValueError("Texts must be of equal length.")
	differentLettersCount = 0
	for i in range(len(text1)):
		if text1[i] != text2[i]:
			differentLettersCount += 1
	return differentLettersCount