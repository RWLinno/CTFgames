from  PIL import Image

import matplotlib.pyplot as plt
from PIL import Image

im = Image.open("src/mozart.jif") #这是oxygen.png黑白部分的位置

def reconstruct(pic,flag):
    # 打开输入图片
    # 创建一个新的图片对象，与输入图片大小和模式相同
    out = Image.new(pic.mode, (pic.width,pic.height))
    for x in range(0,pic.width):
        for y in range(0,pic.height):
            if (x+y)%2 == flag:
                pixel = pic.getpixel((x, y))
                b, g, r = pic[y, x]
                print(b,g,r)
            
                out.putpixel((x,y),pixel)
    # 保存输出图片
    fig, ax = plt.subplots()
    ax.imshow(out)


# 调用函数重构图片，指定输入和输出路径
reconstruct(im,0)