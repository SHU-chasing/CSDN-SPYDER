#-*- coding = utf-8 -*-
#@Time : 2020-10-13 10:44
#@Author : chasing
#@File : testget.py
#@Software: PyCharm

import re
import requests
import parsel
import pdfkit

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"
}
baseUrl='https://blog.csdn.net/qq_27133869'
findBranch=re.compile(r'<a href="(.*?)" target="_blank">')
baseResponse = requests.get(baseUrl, headers=headers)
branchUrls=re.findall(findBranch,baseResponse.text)

assert branchUrls
for j in range(7):
    branchUrls.pop()#删除帮助文档
assert branchUrls#为空直接跳出，节省资源
print(branchUrls)