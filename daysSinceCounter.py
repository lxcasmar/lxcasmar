from datetime import date
import os
from posixpath import relpath
import time

readme = open("README.md","r")
lines = readme.readlines()
today = date.today()
worst_day = date(2014,6,29)
lines[-2] = (str((today-worst_day).days)+lines[-2])

readme = open("README.md","w")
readme.writelines(lines)
readme.close()
