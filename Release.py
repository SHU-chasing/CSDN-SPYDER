#-*- coding = utf-8 -*-
#@Time : 2020-10-12 20:09
#@Author : chasing
#@File : Release.py
#@Software: PyCharm


#导入相应的模块
import re
import requests
import parsel
import pdfkit

def main():
    # Pages=askPages(BaseUrl)
    # print(Pages)
    i=1
    askUrl(baseUrl, i)
    # for i in range(0,100,1):
    #     tempUrl = baseUrl+str(i)
    #     askUrl(tempUrl, i)
    Response()



findChinese=re.compile(r'[\u4e00-\u9fa5]+',re.S)
findBranch=re.compile(r'<a href="(.*?)" target="_blank">')
findFile=re.compile(r'<meta name="keywords" content="(.*?)">', re.S)
# findPages=re.compile(r'<li data-page="(\d+)" class="ui-pager">.*?</li>',re.S)

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"
}
baseUrl='https://blog.csdn.net/gx17864373822/category_10410333.html'
saveUrl='D:\\desktop\\CSDN\\图像处理\\'
# 页面数量为动态
# def askPages(BaseUrl):#js
#     response = requests.get(BaseUrl, headers=headers)
#     print(response.text)
#     Pages = re.findall(FindPages, response.text)
#     return Pages
def askUrl(baseUrl,i):
    baseResponse = requests.get(baseUrl, headers=headers)
    # print(baseResponse.text)
    branchUrls=re.findall(findBranch,baseResponse.text)
    assert branchUrls
    for j in range(7):
        branchUrls.pop()#删除帮助文档
    assert branchUrls#为空直接跳出，节省资源
    # print(branchUrls)
    times=1
    for BranchUrl in branchUrls:
        branchResponse = requests.get(BranchUrl, headers=headers)
        #保存的文件名
        tempTitle = ''.join(re.findall(findFile, branchResponse.text))
        print(tempTitle)
        print(re.findall(findChinese, tempTitle))
        finalTitle = " ".join(re.findall(findChinese, tempTitle))
        print("第 %d 面的 %d 篇文章名为:" %(i, times)+str(finalTitle)+'\n')
        #最终网页源代码
        finalHtml = r'<!doctype html><html><head><meta charset="UTF-8"><title>' + ' '.join(finalTitle) + r'</title></head><body>{content}</body></html>'
        #pdf文件的保存位置
        fileUrl = saveUrl+ ''.join(finalTitle) + '.pdf'
        print("第 %d 面的 %d 篇文章保存路径为:" %(i, times) + str(fileUrl) + '\n')
        selector = parsel.Selector(branchResponse.text)
        article = selector.css('article').get()
        #文件保存的位置
        with open('temp.html', mode='w', encoding='utf-8') as f:
            f.write(finalHtml.format(content=article))
        try:
            config = pdfkit.configuration(wkhtmltopdf='E:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            # config = pdfkit.configuration(wkhtmltopdf=path_wk)
            with open('temp.html', 'r', encoding='utf-8') as f:
                pdfkit.from_file(f, fileUrl, configuration=config)
            print("第 %d 面的 %d 篇文章pdf文件保存成功！" % (i, times)+'\n')
        except:
            print("第 %d 面的 %d 篇文章pdf文件保存失败！" % (i, times)+'\n')
            pass
            # continue
        times+=1
    print("页面 %d 中的所有文件保存成功"%i+'\n')
def Response():
    print("Hello World")
if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
