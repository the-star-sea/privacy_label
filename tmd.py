
import os
dir_path="social/process"
cnt=0
for file in os.listdir(dir_path):
    if file.endswith(".txt"):
        cnt+=1
print(cnt)