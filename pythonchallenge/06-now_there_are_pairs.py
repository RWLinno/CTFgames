# 打开F12有个提示是zip，我们跳转到channel.zip看看
# 发现是个压缩包，有很多txt
# 按照linkedlist的思路一直读下一个文本，最终会在46145.txt提示 "Collect the comments." 
# 因此我们转到压缩包中按顺序把comments串起来试一下

import zipfile
import re

# 指定要读取的ZIP文件的文件名
zip_file_name = 'src/channel.zip'  # 将文件名替换为您要读取的ZIP文件名
nothing = '90052'
ans = []
# 打开ZIP文件
with zipfile.ZipFile(zip_file_name, 'r') as zip_file:
    # 获取ZIP文件中所有文件的名称
    file_names = zip_file.namelist()
    # 遍历ZIP文件中的文件名
    while True:
        # 获取目标txt文件的注释
        txt_file_info = zip_file.getinfo(nothing+'.txt')
        txt_file_comment = txt_file_info.comment.decode('utf-8')
        # 打印目标txt文件的注释
        with open('src/channel/'+nothing+'.txt','r') as txt:
            text = txt.read()
            nxt = re.findall(r'\d+',text)
            if len(nxt):
                nxt = nxt[0]
            else:
                break
            print(text,'next:',nxt)
        nothing = nxt
        ans.append(txt_file_comment)
    print(ans)

# 可以看到输出结果比较诡异，但是隐约串成了单词OXYGEN，输进去就是结果了
# 不过这里可以进一步处理的，不过既然答案出来了我就懒得写了