import unittest
from Song import Song

class SongTest(unittest.TestCase):
	def setUp(self):
		self.song = Song()

	def tearDown(self):
		self.song = None

if __name__ == "__main__":
	unittest.main()