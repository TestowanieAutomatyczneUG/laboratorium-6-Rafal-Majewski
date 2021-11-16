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
	def tearDown(self):
		self.song = None

if __name__ == "__main__":
	unittest.main()