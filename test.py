# d=''
# a=['sad','44']
# c=d.join(a)
# print(c)
import re

line = "YOu are smasdasr are dogs";

searchObj = re.search(r'(.*) are (.*?) (.*)', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")