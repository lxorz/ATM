# -*- coding:utf-8 -*-


from conf import settings


def authenticate(username,password):
    """
    登录认证
    :param username:
    :param password:
    :return:
    """
    if username == settings.ADMIN_ACCOUNT and password == settings.ADMIN_PASSWORD:
        return True
    return False
