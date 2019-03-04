import os

print(os.getcwd())
print(type(os.getcwd()))
def readDevicesList():
    p = os.popen('adb devices')
    devicesList = p.read()
    p.close()
    lists = devicesList.split("\n")
    devicesNames = []
    for item in lists:
        if (item.strip() == ""):
            continue
        elif (item.startswith("List of")):
            continue
        else:
            devicesNames.append(item.split("\t")[0])
    return devicesNames

def readDevices_version():
    try:
        p = os.popen('adb shell getprop ro.build.version.release')
        version = p.read()
        p.close()
        return version
    except AssertionError as a:
        print(str(a))

def get_devices_name():
    try:
        p = os.popen('adb shell getprop ro.product.model')
        name = p.read()
        p.close()
        nn = name.split("\n")
        return nn[0]
    except AssertionError as a:
        print(str(a))

a = get_devices_name()
def mainw():
    print(a,'Start')

if __name__ == '__main__':
    print((readDevicesList())[0])
    print(readDevices_version())
    print(get_devices_name(),'开始执行测试')
    mainw()
