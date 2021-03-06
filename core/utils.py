#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/1/16


def initial():
    """
    初始化目录
    :return:
    """
    import os
    from conf import settings
    if not os.path.exists(settings.LOG_PATH):
        os.mkdir(settings.LOG_PATH)

    if settings.DATABASE['engine'] == 'file_storage':
        if not os.path.exists(settings.DATABASE['file_path']):
            os.mkdir(settings.DATABASE['file_path'])
        for table in settings.DATABASE['tables']:
            if not os.path.exists(settings.DATABASE['tables'][table]['file_path']):
                os.mkdir(settings.DATABASE['tables'][table]['file_path'])


def format_result(action):
    """
    处理操作结果
    :param action:
    :return:
    """

    def hook_action(**kwargs):
        ret = action(**kwargs)
        if isinstance(ret,dict):
            status = ret.get('status', 0)
            if status < 0:
                print(ret['status'])
                return False
            logger = ret.get('logger', False)
            if logger:
                logger.info(ret['msg'])
                if 'print' not in ret or ret['print']:
                    print("\033[92m操作成功,\033[0m操作内容：%s" % ret['msg'])
                return True
        return False

    return hook_action


def hash_md5(content):
    """
    md5文本加密
    :param content:
    :return:
    """
    import hashlib
    encypt = hashlib.md5()
    encypt.update(bytes(content, encoding='utf-8'))
    return encypt.hexdigest()


def calculate_date(years=0, months=0, days=0, time_format=False):
    """
    日期加减
    :param years:
    :param months:
    :param days:
    :param time_format:
    :return:
    """
    import datetime
    date_formatter = "%Y-%m-%d"
    if time_format:
        date_formatter = "%Y-%m-%d %H:%M:%S"
    dt = datetime.datetime.now()
    return dt.replace(year=dt.year + years, month=dt.month + months, day=dt.day + days).strftime(date_formatter)


def format_table(header, records):
    """
    格式化输出查询结果
    :param header: 标题头
    :param records:
    :return:
    """
    print("".join(["\033[94m%s\033[0m" % i.center(32).title() for i in header]))
    for record in records:
        print("".join([str(record[i]).center(32) for i in record]))
    print("共有\033[92m%d\033[0m条记录" % len(records))


def append_symbol(content, start='"', end='"'):
    """
    在前后追加指定字符
    :param content:
    :param start:
    :param end:
    :return:
    """
    return "%s%s%s" % (start, content, end)


def strip_extend(string):
    """
    去除空白双引号单引号
    :param string:
    :return:
    """
    return string.strip().strip('"').strip("'")


def is_float_num(string):
    """
    正则判断浮点字符
    :param string:
    :return:
    """
    import re
    ret = re.search('^-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0)$', string)
    return ret


def format_status(status):
    """
    格式化状态
    :param status:
    :return:
    """
    return '\033[91m禁用\033[0m' if int(status) else '\033[92m正常\033[0m'


def format_transaction(trans_type):
    """
    格式化交易类型
    :param trans_type:
    :return:
    """
    from conf import settings
    if trans_type not in settings.TRANSACTION_TYPE.keys() or 'title' not in settings.TRANSACTION_TYPE[trans_type]:
        return '未知类型'
    return settings.TRANSACTION_TYPE[trans_type]['title']
