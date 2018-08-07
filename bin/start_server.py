# -*- coding:utf-8 -*-
# Author: LiuXing 
# date: 7/26/2018 9:56 PM
import os
import sys

from atm import main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == '__main__':
    #程序总入口
    main.run()