import unittest
from assessment_two import AssessmentTwo


class TestAssessmentTwo(unittest.TestCase):

    def setUp(self):
        self.exam = AssessmentTwo()

    # ===== BASIC =====

    def test_count_negative_numbers(self):
        self.assertEqual(self.exam.count_negative_numbers([-1, 2, -3, 4]), 2)
        self.assertEqual(self.exam.count_negative_numbers([1, 2, 3]), 0)
        self.assertEqual(self.exam.count_negative_numbers([]), 0)

    def test_average(self):
        self.assertEqual(self.exam.average([2, 4, 6]), 4)
        self.assertEqual(self.exam.average([1]), 1)
        self.assertIsNone(self.exam.average([]))

    def test_first_and_last(self):
        self.assertEqual(self.exam.first_and_last([1, 2, 3]), (1, 3))
        self.assertEqual(self.exam.first_and_last(["a"]), ("a", "a"))
        self.assertIsNone(self.exam.first_and_last([]))

    def test_count_consonants(self):
        self.assertEqual(self.exam.count_consonants("Hello"), 3)
        self.assertEqual(self.exam.count_consonants("AEIOU"), 0)
        self.assertEqual(self.exam.count_consonants("bcd!"), 3)

    def test_is_even_length(self):
        self.assertTrue(self.exam.is_even_length("test"))
        self.assertFalse(self.exam.is_even_length("odd"))
        self.assertTrue(self.exam.is_even_length(""))


    # ===== INTERMEDIATE =====

    def test_remove_duplicates_preserve_order(self):
        self.assertEqual(
            self.exam.remove_duplicates_preserve_order([1, 2, 2, 3, 1]),
            [1, 2, 3]
        )
        self.assertEqual(self.exam.remove_duplicates_preserve_order([]), [])

    def test_word_lengths(self):
        self.assertEqual(
            self.exam.word_lengths("hello world"),
            {"hello": 5, "world": 5}
        )
        self.assertEqual(self.exam.word_lengths(""), {})

    def test_second_largest(self):
        self.assertEqual(self.exam.second_largest([5, 1, 3, 4]), 4)
        self.assertIsNone(self.exam.second_largest([10]))
        self.assertIsNone(self.exam.second_largest([]))

    def test_chunk_list(self):
        self.assertEqual(
            self.exam.chunk_list([1, 2, 3, 4, 5], 2),
            [[1, 2], [3, 4], [5]]
        )
        self.assertEqual(self.exam.chunk_list([], 3), [])

    def test_is_anagram(self):
        self.assertTrue(self.exam.is_anagram("listen", "silent"))
        self.assertTrue(self.exam.is_anagram("Dormitory", "Dirty room"))
        self.assertFalse(self.exam.is_anagram("hello", "world"))


    # ===== ADVANCED =====

    def test_running_sum(self):
        self.assertEqual(
            self.exam.running_sum([1, 2, 3]),
            [1, 3, 6]
        )
        self.assertEqual(self.exam.running_sum([]), [])

    def test_longest_unique_substring(self):
        self.assertEqual(self.exam.longest_unique_substring("abcabcbb"), 3)
        self.assertEqual(self.exam.longest_unique_substring("bbbbb"), 1)
        self.assertEqual(self.exam.longest_unique_substring(""), 0)

    def test_rotate_matrix_90(self):
        self.assertEqual(
            self.exam.rotate_matrix_90([[1, 2], [3, 4]]),
            [[3, 1], [4, 2]]
        )

    def test_validate_palindrome_number(self):
        self.assertTrue(self.exam.validate_palindrome_number(121))
        self.assertFalse(self.exam.validate_palindrome_number(123))
        self.assertTrue(self.exam.validate_palindrome_number(0))

    def test_generate_pascal_row(self):
        self.assertEqual(self.exam.generate_pascal_row(0), [1])
        self.assertEqual(self.exam.generate_pascal_row(1), [1, 1])
        self.assertEqual(self.exam.generate_pascal_row(4), [1, 4, 6, 4, 1])


if __name__ == "__main__":
    unittest.main()