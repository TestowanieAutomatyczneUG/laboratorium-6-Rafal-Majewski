import unittest
from hammingDistance import hammingDistance

class HammingTest(unittest.TestCase):
	def test_empty_strands(self):
		self.assertEqual(hammingDistance("", ""), 0)
	
	def test_single_letter_identical_strands(self):
		self.assertEqual(hammingDistance("A", "A"), 0)
	@unittest.skip("Not implemented yet")
	def test_single_letter_different_strands(self):
		self.assertEqual(hammingDistance("G", "T"), 1)
	@unittest.skip("Not implemented yet")
	def test_long_identical_strands(self):
		self.assertEqual(hammingDistance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)
	@unittest.skip("Not implemented yet")
	def test_long_different_strands(self):
		self.assertEqual(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT"), 9)
	@unittest.skip("Not implemented yet")
	def test_disallow_first_strand_longer(self):
		with self.assertRaisesWithMessage(ValueError):
			hammingDistance("AATG", "AAA")
	@unittest.skip("Not implemented yet")
	def test_disallow_second_strand_longer(self):
		with self.assertRaisesWithMessage(ValueError):
			hammingDistance("ATA", "AGTG")
	@unittest.skip("Not implemented yet")
	def test_disallow_left_empty_strand(self):
		with self.assertRaisesWithMessage(ValueError):
			hammingDistance("", "G")
	@unittest.skip("Not implemented yet")
	def test_disallow_right_empty_strand(self):
		with self.assertRaisesWithMessage(ValueError):
			hammingDistance("G", "")

	# Utility functions
	def setUp(self):
		try:
			self.assertRaisesRegex
		except AttributeError:
			self.assertRaisesRegex = self.assertRaisesRegexp

	def assertRaisesWithMessage(self, exception):
		return self.assertRaisesRegex(exception, r".+")

if __name__ == "__main__":
	unittest.main()