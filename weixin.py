#-*- coding = utf-8 -*-
#@Time : 2020-10-17 23:43
#@Author : chasing
#@Email : 643601464@qq.com
#@File : weixin.py
#@Software: PyCharm


def main():
    import re
    import requests
    import parsel
    import pdfkit
    BranchUrl = 'https://mp.weixin.qq.com/s?__biz=Mzg2NTAzMTExNg==&mid=2247483866&idx=1&sn=fe987cd24448bd6eb2138cfd43a82cf8&chksm=ce610779f9168e6ff1a7e035517d5163e03fa6229a7688eb18dfd70780fe6980fbdd8728d0f0&mpshare=1&scene=23&srcid=1017pm6WSs3bLokWby6c2itK&sharer_sharetime=1602949317981&sharer_shareid=4e08b3c4da5fdd6e1ae7c2c8653e6f12#rd'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38'}
    response = requests.get(BranchUrl, headers=headers)
    with open('1.html', mode='w', encoding='utf-8') as f:
        f.write(response.text)
    config = pdfkit.configuration(wkhtmltopdf='E:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_file('1.html','D:\\desktop\\1.pdf' , configuration=config)
    print("Hello World!")

if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()