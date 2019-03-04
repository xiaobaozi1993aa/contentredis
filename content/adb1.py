import os

p = os.popen('adb shell am start -W com.sz.gcyh.KSHongBao/com.guochuang.mimedia.ui.activity.WelcomeActivity')
name = p.read()
print(name)
print(type(name))




