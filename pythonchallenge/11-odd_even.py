# F12没有隐藏的信息了，观察图片发现亮暗像素相邻，再结合odd even这个题目，
# 我们将将图片的奇数/偶数位分别重组看看结果

import matplotlib.pyplot as plt
from PIL import Image

im = Image.open("src/cave.jpg") #这是oxygen.png黑白部分的位置

def reconstruct(pic,flag):
    # 打开输入图片
    # 创建一个新的图片对象，与输入图片大小和模式相同
    out = Image.new(pic.mode, (pic.width//2,pic.height//2))
    for x in range(0,pic.width):
        for y in range(0,pic.height):
            if (x+y)%2 == flag:
                pixel = pic.getpixel((x, y))
                out.putpixel((x//2,y//2),pixel)
    # 保存输出图片
    fig, ax = plt.subplots()
    ax.imshow(out)


# 调用函数重构图片，指定输入和输出路径
reconstruct(im,0)
reconstruct(im,1)
plt.show()

# 得到了evil单词，输进去的网站居然还要密码？浏览器帮我记了前面那个密码居然通过了？？？
# 感觉是个bug，事实上http://www.pythonchallenge.com/pc/return/evil.html 是直接能进的
'''
username = huge
password = file
'''