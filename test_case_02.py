"""
* 编写的模块，建议小写test开头
* test_case_02
* s
"""
import unittest


from login import get_username, get_password

# 使用TestCase

version = 2.0

class TestLogin(unittest.TestCase):
    # 所编写的测试用例，必须是一个类，而且必须继承TestCase类
    # 编写测试类，建议以Test开头

    # 类的初始化方法
    @classmethod  # 装饰器
    def setUpClass(cls) -> None:

        print('setUpClass : 执行类之前调用一次')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass 执行类之后调用一次')

    # 初始化方法
    def setUp(self) -> None:
        print('setUp 每次执行用例前执行')

    def tearDown(self) -> None:
        print('tearDown 每次执行用例后执行')

    def test_login_username(self):
        print('获取用户名测试用例')
        # 每个测试方法，都是以test开头

        # 预期结果 : 本人登录的账号
        expect_username = 'test01'
        # 实际结果 : 显示在页面上的账号
        acut_username = get_username()
        # assert expect_username == acut_username
        self.assertEqual(expect_username, acut_username)
    """
    @unittest.skip('跳过此测试用例:')
    # 再Run窗口内会显示ignored:1s
    """
    @unittest.skipIf(version>3.0,'执行此用例')
    # True 执行 skip 跳过
    # False 不执行 skip 跳过,此条测试用会执行

    def test_login_password(self):
        print('获取密码测试用例')
        # 预期结果 : 本人登录账号的密码
        expect_password = 'test01'
        # 实际结果 : 显示在页面上的密码
        acut_password = get_password()
        # assert expect_password == acut_password
        self.assertEqual(expect_password, acut_password)

# 利用unittest执行测试用例,结果内包含执行了多条


# unittest.main()
# 把这个方法放出来会提示No tests were found
# unittest.main(),主方法


"""
# 创建一个测试套件，套件可以理解为一组测试用例的组合
suite = unittest.TestSuite()
# 添加单个用例
"""

# 1.通过TestSuite中的addTest添加测试方法 一个测试方法等同于一条测试用例目前可以理解为
"""
suite.addTest(TestLogin('test_login_username'))
suite.addTest(TestLogin('test_login_password'))
"""

# 2.通过TestSuite中addTests添加测试方法
# 添加多条测试用例:addTests
"""
lst = [TestLogin('test_login_username'),TestLogin('test_login_password')]
suite.addTests(lst)
"""

# 3.通过TestLoader()中discover添加测试方法
# TestLoader
# 用来加载TestCase到TestSuite中，即加载满足条件的测试用例，并把测试用例封装成测试套件。
# suite = unittest.TestLoader().discover(test_dir,pattern = 'test*.py')
# test_dir 路径 test*.py 类似文件

# 使用TestLoader中的discover来执行测试用例

suite = unittest.TestLoader().discover('.', pattern='test*.py')

# 当前路径下的测试模块,一并执行,不再用指定测试方法


# TextTestRunner() 是一个类 用其中的 run() 来运行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)
