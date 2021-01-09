import subprocess

s = subprocess.call(["ls", "-l"])
print(s)
s = subprocess.check_output(["ls", "-l"])
print(s)
s = subprocess.check_call(["ls", "-l"])
print(s)

p1 = subprocess.Popen(['dmesg'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "hda"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)