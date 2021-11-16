import unittest
from Song import Song

class SongTest(unittest.TestCase):
	def setUp(self):
		self.song = Song()
	def test_getLine_0(self):
		self.assertEqual(self.song.getLine(0), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

	def tearDown(self):
		self.song = None

if __name__ == "__main__":
	unittest.main()