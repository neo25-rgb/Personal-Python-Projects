import unittest
from assessment_three import AssessmentThree


class TestAssessmentThree(unittest.TestCase):

    def setUp(self):
        self.exam = AssessmentThree()

    # ===== BASIC =====

    def test_count_truthy(self):
        self.assertEqual(self.exam.count_truthy([True, False, 1, 0, "a", ""]), 3)
        self.assertEqual(self.exam.count_truthy([]), 0)

    def test_clamp(self):
        self.assertEqual(self.exam.clamp(5, 1, 10), 5)
        self.assertEqual(self.exam.clamp(-1, 0, 5), 0)
        self.assertEqual(self.exam.clamp(100, 0, 50), 50)

    def test_remove_whitespace(self):
        self.assertEqual(self.exam.remove_whitespace("a b\tc\nd"), "abcd")
        self.assertEqual(self.exam.remove_whitespace(""), "")

    def test_all_unique(self):
        self.assertTrue(self.exam.all_unique([1, 2, 3]))
        self.assertFalse(self.exam.all_unique([1, 2, 2]))
        self.assertTrue(self.exam.all_unique([]))

    def test_title_case(self):
        self.assertEqual(self.exam.title_case("hello world"), "Hello World")
        self.assertEqual(self.exam.title_case("python"), "Python")


    # ===== INTERMEDIATE =====

    def test_frequency_sort(self):
        self.assertEqual(
            self.exam.frequency_sort([4, 4, 1, 2, 2, 2]),
            [1, 4, 4, 2, 2, 2]
        )

    def test_merge_intervals(self):
        self.assertEqual(
            self.exam.merge_intervals([[1,3],[2,6],[8,10]]),
            [[1,6],[8,10]]
        )

    def test_longest_word_length(self):
        self.assertEqual(self.exam.longest_word_length("The quick brown fox"), 5)
        self.assertEqual(self.exam.longest_word_length(""), 0)

    def test_prefix_sums(self):
        self.assertEqual(
            self.exam.prefix_sums([1, 2, 3]),
            [1, 3, 6]
        )

    def test_valid_binary_string(self):
        self.assertTrue(self.exam.valid_binary_string("101010"))
        self.assertFalse(self.exam.valid_binary_string("10201"))
        self.assertFalse(self.exam.valid_binary_string(""))


    # ===== ADVANCED =====

    def test_product_except_self(self):
        self.assertEqual(
            self.exam.product_except_self([1, 2, 3, 4]),
            [24, 12, 8, 6]
        )

    def test_spiral_order(self):
        self.assertEqual(
            self.exam.spiral_order([[1,2,3],[4,5,6],[7,8,9]]),
            [1,2,3,6,9,8,7,4,5]
        )

    def test_longest_palindromic_substring(self):
        self.assertEqual(
            self.exam.longest_palindromic_substring("babad"),
            "bab"
        )
        self.assertEqual(
            self.exam.longest_palindromic_substring("cbbd"),
            "bb"
        )

    def test_count_islands(self):
        grid = [
            ["1","1","0","0"],
            ["1","0","0","1"],
            ["0","0","1","1"]
        ]
        self.assertEqual(self.exam.count_islands(grid), 3)

    def test_validate_sudoku(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertTrue(self.exam.validate_sudoku(board))


if __name__ == "__main__":
    unittest.main()