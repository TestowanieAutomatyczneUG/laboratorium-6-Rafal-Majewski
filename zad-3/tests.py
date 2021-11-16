import unittest
from Song import Song

class SongTest(unittest.TestCase):
	def setUp(self):
		self.song = Song()
	def test_getLine_1(self):
		self.assertEqual(self.song.getLine(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")
	def test_getLine_200(self):
		self.assertRaises(IndexError, self.song.getLine, 200)
	def test_getLine_0(self):
		self.assertRaises(IndexError, self.song.getLine, 0)
	def test_getLine_2_dot_5(self):
		self.assertRaises(IndexError, self.song.getLine, 2.5)
	def test_getLine_4(self):
		self.assertEqual(self.song.getLine(4), "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")
	
	def test_getLines_1_to_1(self):
		self.assertEqual(self.song.getLines(1, 1), ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."])

	def test_getLines_1_to_minus_10(self):
		self.assertRaises(IndexError, self.song.getLines, 1, -10)
	
	def test_getLines_2_to_3(self):
		self.assertEqual(self.song.getLines(2, 3), [
			"On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
		])
	
	def test_getLines_14_to_20(self):
		self.assertRaises(IndexError, self.song.getLines, 14, 20)

	def test_getLines_to_3(self):
		self.assertEqual(self.song.getLines(endLineNumber = 3), [
			"On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
			"On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
		])

	def test_getLines_from_13(self):
		self.assertRaises(IndexError, self.song.getLines, startLineNumber = 13)

	def test_getLines_from_10(self):
		self.assertEqual(self.song.getLines(startLineNumber = 10), [
			"On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
		])

	def test_getAllLines(self):
		self.assertEqual(self.song.getAllLines(), [
			"On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
			"On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
			"On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
		])

	def tearDown(self):
		self.song = None

if __name__ == "__main__":
	unittest.main()