from datetime import date
import os
from posixpath import relpath
import time

readme = open("README.md","r")
lines = readme.readlines()
today = date.today()
worst_day = date(2014,6,29)
# There's some weird formatting with the newline... just get it to work w readme file
lines[-2] = (lines[-2][0:-5]+str((today-worst_day).days)+"\n")

readme = open("README.md","w")
readme.writelines(lines)
readme.close()
