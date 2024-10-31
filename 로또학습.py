# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:02:29 2024

@author: Rogio
"""


from page3.get_data import Lotto_class

import pandas as pd


# Lotto_class의 인스턴스 생성
lotto_instance = Lotto_class()


최근회차 = lotto_instance.최근회차()

과거기록 = lotto_instance.download_records(1, 최근회차)