import unittest
from parameterized import parameterized
# 实现加法的方法


def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):

    # def test_add_01(self):
    #     res1 = add(1, 1)
    #     self.assertEqual(2, res1)
    #     # 期望值是否和运行结果一致
    #
    # def test_add_02(self):
    #     res2 = add(1, 0)
    #     self.assertEqual(1, res2)
    #
    # def test_add_03(self):
    #     res3 = add(-1, 2)
    #     self.assertEqual(1, res3)
    #
    # """
    # 以上三个测试方法，出现了代码冗余。
    # 下面进行优化,for循环
    # """
    #
    # def test_add(self):
    #     test_data = [(1, 1, 2), (1, 0, 1), (-1, 2, 1)]
    #
    #     """
    #     for x in  test_data:
    #         # 取出来是一个元组
    #     """
    #
    #     for x, y, expect_value in test_data:
    #         res = add(x, y)
    #         self.assertEqual(res, expect_value)
    @parameterized.expand([(1, 1, 2), (1, 0, 1), (-1, 2, 1), (0, 0, 0)])
    def test_add(self, a, b, result):
        res = add(a, b)
        # res 实际结果
        self.assertEqual(result, res)  # result 是预期结果 res 是实际结果

# 断言 : 测试 / 对两个值进行比较 (大于 等于 小于)


if __name__ == '__main__':
    unittest.main()
