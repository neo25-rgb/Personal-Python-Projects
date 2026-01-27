import unittest
from practice_questions import PracticeExam


class TestPracticeExam(unittest.TestCase):

    def setUp(self):
        self.exam = PracticeExam()

    # ===== BASIC QUESTIONS =====

    def test_count_odd_numbers(self):
        self.assertEqual(self.exam.count_odd_numbers([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.exam.count_odd_numbers([2, 4, 6]), 0)
        self.assertEqual(self.exam.count_odd_numbers([]), 0)
        self.assertEqual(self.exam.count_odd_numbers([1]), 1)

    def test_sum_list(self):
        self.assertEqual(self.exam.sum_list([1, 2, 3]), 6)
        self.assertEqual(self.exam.sum_list([-1, 1]), 0)
        self.assertEqual(self.exam.sum_list([]), 0)
        self.assertEqual(self.exam.sum_list([10]), 10)

    def test_reverse_words_order(self):
        self.assertEqual(
            self.exam.reverse_words_order("hello world python"),
            "python world hello"
        )
        self.assertEqual(
            self.exam.reverse_words_order("one"),
            "one"
        )
        self.assertEqual(
            self.exam.reverse_words_order("a b c"),
            "c b a"
        )

    def test_contains_vowel(self):
        self.assertTrue(self.exam.contains_vowel("skyA"))
        self.assertTrue(self.exam.contains_vowel("HELLO"))
        self.assertFalse(self.exam.contains_vowel("rhythm"))
        self.assertFalse(self.exam.contains_vowel(""))

    def test_smallest_number(self):
        self.assertEqual(self.exam.smallest_number([5, 3, 9]), 3)
        self.assertEqual(self.exam.smallest_number([-5, -10, 0]), -10)
        self.assertEqual(self.exam.smallest_number([7]), 7)
        self.assertIsNone(self.exam.smallest_number([]))


    # ===== INTERMEDIATE QUESTIONS =====

    def test_remove_vowels(self):
        self.assertEqual(self.exam.remove_vowels("Hello World"), "Hll Wrld")
        self.assertEqual(self.exam.remove_vowels("AEIOUaeiou"), "")
        self.assertEqual(self.exam.remove_vowels("Python"), "Pythn")
        self.assertEqual(self.exam.remove_vowels(""), "")

    def test_count_character_frequency(self):
        self.assertEqual(
            self.exam.count_character_frequency("aab"),
            {"a": 2, "b": 1}
        )
        self.assertEqual(
            self.exam.count_character_frequency("abc"),
            {"a": 1, "b": 1, "c": 1}
        )
        self.assertEqual(
            self.exam.count_character_frequency(""),
            {}
        )

    def test_is_prime(self):
        self.assertTrue(self.exam.is_prime(2))
        self.assertTrue(self.exam.is_prime(13))
        self.assertFalse(self.exam.is_prime(1))
        self.assertFalse(self.exam.is_prime(0))
        self.assertFalse(self.exam.is_prime(-7))
        self.assertFalse(self.exam.is_prime(9))

    def test_flatten_list(self):
        self.assertEqual(
            self.exam.flatten_list([[1, 2], [3, 4]]),
            [1, 2, 3, 4]
        )
        self.assertEqual(
            self.exam.flatten_list([[1], [], [2, 3]]),
            [1, 2, 3]
        )
        self.assertEqual(
            self.exam.flatten_list([]),
            []
        )

    def test_longest_common_prefix(self):
        self.assertEqual(
            self.exam.longest_common_prefix(["flower", "flow", "flight"]),
            "fl"
        )
        self.assertEqual(
            self.exam.longest_common_prefix(["dog", "racecar", "car"]),
            ""
        )
        self.assertEqual(
            self.exam.longest_common_prefix(["single"]),
            "single"
        )
        self.assertEqual(
            self.exam.longest_common_prefix([]),
            ""
        )


    # ===== ADVANCED QUESTIONS =====

    def test_fibonacci_sequence(self):
        self.assertEqual(
            self.exam.fibonacci_sequence(1),
            [0]
        )
        self.assertEqual(
            self.exam.fibonacci_sequence(2),
            [0, 1]
        )
        self.assertEqual(
            self.exam.fibonacci_sequence(5),
            [0, 1, 1, 2, 3]
        )
        self.assertEqual(
            self.exam.fibonacci_sequence(0),
            []
        )

    def test_max_subarray_sum(self):
        self.assertEqual(
            self.exam.max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]),
            6
        )
        self.assertEqual(
            self.exam.max_subarray_sum([1, 2, 3]),
            6
        )
        self.assertEqual(
            self.exam.max_subarray_sum([-5, -1, -8]),
            -1
        )
        self.assertEqual(
            self.exam.max_subarray_sum([0]),
            0
        )

    def test_valid_parentheses(self):
        self.assertTrue(self.exam.valid_parentheses("()"))
        self.assertTrue(self.exam.valid_parentheses("({[]})"))
        self.assertFalse(self.exam.valid_parentheses("(]"))
        self.assertFalse(self.exam.valid_parentheses("((())"))
        self.assertTrue(self.exam.valid_parentheses(""))

    def test_rotate_left(self):
        self.assertEqual(
            self.exam.rotate_left([1, 2, 3, 4, 5], 2),
            [3, 4, 5, 1, 2]
        )
        self.assertEqual(
            self.exam.rotate_left([1, 2, 3], 3),
            [1, 2, 3]
        )
        self.assertEqual(
            self.exam.rotate_left([1, 2, 3], 4),
            [2, 3, 1]
        )
        self.assertEqual(
            self.exam.rotate_left([], 5),
            []
        )

    def test_spiral_matrix(self):
        self.assertEqual(
            self.exam.spiral_matrix(1),
            [[1]]
        )
        self.assertEqual(
            self.exam.spiral_matrix(2),
            [[1, 2],
             [4, 3]]
        )
        self.assertEqual(
            self.exam.spiral_matrix(3),
            [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
        )


if __name__ == "__main__":
    unittest.main()