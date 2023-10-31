# 打开开发者工具，看到提示信息是叫我们找下面文段中的稀少的字母
# 我们将信息存为文本去处理就好了

with open("src/find.txt") as file:
    txt = file.read()
    for i in txt:
        if i>='a' and i<='z':
            print(i,end='')

# 得到了单词equality，也就是下一关的链接为http://www.pythonchallenge.com/pc/def/equality.html
