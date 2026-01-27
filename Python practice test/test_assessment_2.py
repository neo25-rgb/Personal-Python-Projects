from assessment_2 import * 

class TestFunctions(unittest.TestCase):

    def test_merge_arrays(self):
        self.assertEqual(merge_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_arrays([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_arrays([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge_arrays([1, 2, 3], [1, 2, 3]), [1, 1, 2, 2, 3, 3])

    def test_intersection_of_arrays(self):
        self.assertEqual(intersection_of_arrays([1, 2, 3], [2, 3, 4]), [2, 3])
        self.assertEqual(intersection_of_arrays([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(intersection_of_arrays([1, 1, 2], [2, 2, 3]), [2])
        self.assertEqual(intersection_of_arrays([], [1, 2, 3]), [])

    def test_fibonacci_dp(self):
        self.assertEqual(fibonacci_dp(0), 0)
        self.assertEqual(fibonacci_dp(1), 1)
        self.assertEqual(fibonacci_dp(5), 5)
        self.assertEqual(fibonacci_dp(10), 55)

    def test_reverse_string_words(self):
        self.assertEqual(reverse_string_words("Hello World"), "World Hello")
        self.assertEqual(reverse_string_words("Python is great"), "great is Python")
        self.assertEqual(reverse_string_words("Test"), "Test")
        self.assertEqual(reverse_string_words(""), "")

    def test_remove_duplicates_from_string(self):
        self.assertEqual(remove_duplicates_from_string("aabbcc"), "abc")
        self.assertEqual(remove_duplicates_from_string("abcabc"), "abc")
        self.assertEqual(remove_duplicates_from_string("zzz"), "z")
        self.assertEqual(remove_duplicates_from_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("Hello World"))
        self.assertTrue(is_palindrome("Madam"))
        self.assertFalse(is_palindrome("Python"))

    def test_move_zeros(self):
        self.assertEqual(move_zeros([0, 1, 2, 0, 3, 4]), [1, 2, 3, 4, 0, 0])
        self.assertEqual(move_zeros([0, 0, 0]), [0, 0, 0])
        self.assertEqual(move_zeros([1, 2, 3]), [1, 2, 3])
        self.assertEqual(move_zeros([0]), [0])

    def test_reverse_integer(self):
        self.assertEqual(reverse_integer(123), 321)
        self.assertEqual(reverse_integer(-123), -321)
        self.assertEqual(reverse_integer(0), 0)
        self.assertEqual(reverse_integer(120), 21)

    def test_longest_substring_without_repeating(self):
        self.assertEqual(longest_substring_without_repeating("abcabcbb"), 3)
        self.assertEqual(longest_substring_without_repeating("bbbbb"), 1)
        self.assertEqual(longest_substring_without_repeating("pwwkew"), 3)
        self.assertEqual(longest_substring_without_repeating(""), 0)

    def test_is_anagram(self):
        self.assertTrue(is_anagram("anagram", "nagaram"))
        self.assertFalse(is_anagram("rat", "car"))
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertFalse(is_anagram("hello", "world"))

    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([1, 2, 4, 5]), 3)
        self.assertEqual(find_missing_number([1, 3, 4, 5]), 2)
        self.assertEqual(find_missing_number([1, 2, 3, 4, 5]), 6)
        self.assertEqual(find_missing_number([2, 3, 4]), 1)


    def test_remove_duplicates_from_sorted_array(self):
        self.assertEqual(remove_duplicates_from_sorted_array([1, 1, 2]), 2)
        self.assertEqual(remove_duplicates_from_sorted_array([0, 0, 1, 1, 2, 2]), 3)
        self.assertEqual(remove_duplicates_from_sorted_array([1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(remove_duplicates_from_sorted_array([1]), 1)

    def test_search_insert_position(self):
        self.assertEqual(search_insert_position([1, 3, 5, 6], 5), 2)
        self.assertEqual(search_insert_position([1, 3, 5, 6], 2), 1)
        self.assertEqual(search_insert_position([1, 3, 5, 6], 7), 4)
        self.assertEqual(search_insert_position([1, 3, 5, 6], 0), 0)

    def test_max_subarray_sum(self):
        self.assertEqual(max_subarray_sum([1, -2, 3, -1, 2]), 4)
        self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_subarray_sum([5, 4, -1, 7, 8]), 23)
        self.assertEqual(max_subarray_sum([-1, -2, -3]), -1)

    def test_str_str(self):
        self.assertEqual(str_str("hello", "ll"), 2)
        self.assertEqual(str_str("aaaaa", "bba"), -1)
        self.assertEqual(str_str("mississippi", "issip"), 4)
        self.assertEqual(str_str("abcdef", "def"), 3)

    def test_count_and_say(self):
        self.assertEqual(count_and_say(1), "1")
        self.assertEqual(count_and_say(4), "1211")
        self.assertEqual(count_and_say(5), "111221")
        self.assertEqual(count_and_say(6), "312211")

    def test_climbing_stairs(self):
        self.assertEqual(climbing_stairs(2), 2)
        self.assertEqual(climbing_stairs(3), 3)
        self.assertEqual(climbing_stairs(4), 5)
        self.assertEqual(climbing_stairs(5), 8)

    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        self.assertEqual(two_sum([1, 2, 3], 5), [1, 2])

    def test_is_valid_parentheses(self):
        self.assertTrue(is_valid_parentheses("()"))
        self.assertFalse(is_valid_parentheses("([)]"))
        self.assertTrue(is_valid_parentheses("{[]}"))
        self.assertFalse(is_valid_parentheses("(]"))

if __name__ == '__main__':
    unittest.main()