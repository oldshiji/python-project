import os

os.popen("cd c")
print(os.popen("dir"))

for line in os.popen("dir"):
    print(line)