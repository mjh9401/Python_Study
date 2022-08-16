# 내장 모듈 : 파이썬 설치시 자동으로 설치되는 모듈

from math import pi, ceil as c

print(pi)
print(c(2.3))

# 외부 모듈 : 다른사람이 만든 파이썬 파일 pip로 설치해서 사용
# pyautogui

import pyautogui as pg

pg.moveTo(500, 500, duration=2)

