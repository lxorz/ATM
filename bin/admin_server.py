# -*- coding:utf-8 -*-


import os
import sys
from admin import main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':
    main.run()