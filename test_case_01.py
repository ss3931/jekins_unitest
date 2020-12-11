from  login import get_username,get_password

def test_login_username():
    # 预期结果 : 本人登录的账号
    expect_username = 'test01'
    # 实际结果 : 显示在页面上的账号
    acut_username = get_username()
    assert expect_username == acut_username


def test_login_password():
    # 预期结果 : 本人登录账号的密码
    expect_password = 'test01'
    # 实际结果 : 显示在页面上的密码
    acut_password = get_password()
    assert expect_password == acut_password

# 两个测试用例,缺点一百个测试用例,就要调用一百次方法,也不知道几条成功几条失败
test_login_username()
test_login_password()