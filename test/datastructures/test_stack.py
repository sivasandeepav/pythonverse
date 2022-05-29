import unittest

from datastructures.stack import ArrayStack


class TestStack(unittest.TestCase):
    def test_array_stack(self):
        stack = ArrayStack(10)

        # test empty stack
        self.assertEqual(0, len(stack))
        self.assertEqual(True, stack.is_empty())

        stack.push(1)
        stack.push(2)
        stack.push(3)

        # test __iter__
        it = iter(stack)
        self.assertEqual(3, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(1, next(it))
        self.assertRaises(StopIteration, next, it)

        # test non emptyness
        self.assertEqual(False, stack.is_empty())
        self.assertEqual(3, len(stack))
        self.assertEqual(3, stack.peek())

        # test pop
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())

        # test error cases
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)


if __name__ == '__main__':
    unittest.main()
