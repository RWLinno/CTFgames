# 图片中间黑白色块就是关键信息，先把颜色读出来
# 一开始我气死了，我用截图得到了完全不一样的色块没法做……
# 果然还是要读原图才行
from PIL import Image

im = Image.open("src/oxygen.png") #这是oxygen.png黑白部分的位置

st = []

#for y in range(im.size[1]):
y = im.size[1]//2
for x in range(im.size[0]):
    pix = im.getpixel((x,y))
    st.append(pix[0])
#for i in st:
#    print(i)

# 发现RGB相同，换成字符试试
lst = '.'
for i in st:
    if not chr(i) == lst:
        print(chr(i),end='')
    lst = chr(i)
print("")
#smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]rpngbemkejlfca^_ba_ac
# 手动换成小写字母
next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in next_level:
    print(chr(i),end='')

#得到答案integrity

