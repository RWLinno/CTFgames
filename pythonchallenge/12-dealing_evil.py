# 傻逼题

# 图片叫evil1.jpg,那我们输入evil2.jpg找到第二张图片，得到信息 "not jpg, -.gfx"
# 如果再输入evil3.jpg,会提示我们不要再用同样的方法前进了
# 但是我们再输入evil4.jpg，虽然图片裂了，但是能够在F12元素那里看到信息 “Bert is evil! go back!”
# 输入bert.html发现bert.gif

# dealing evil -> 发牌? deal cards
# 输入cards.html -> 得到彩蛋“wow! you are a genius!”

# 通过根据提示输入evil2.gfx得到一个未知文件，感觉有点怪
# !! 按evil1.jpg的灵感将其分为5等份(要每隔5位取)，得到五张图片

pic = open("src/evil2.gfx",'rb').read()
for i in range(5):
    f = open(f"src/gfx/{i}.jpg",'wb')
    f.write(pic[i::5])
    f.close()

# 将图片上的单词拼在一起 -> dis pro port ional (ity)
# 答案为http://www.pythonchallenge.com/pc/return/disproportional.html