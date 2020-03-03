import re, subprocess

def check_CPU_temp():
    temp = None
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)   # https://stackoverflow.com/a/49563120/3904031
        try:
            temp = float(m.group())
        except:
            pass
    return temp, msg

temp, msg = check_CPU_temp()

print ("temperature (" + u'\xb0' + "C): ", temp)
print ("full message:    ", msg)