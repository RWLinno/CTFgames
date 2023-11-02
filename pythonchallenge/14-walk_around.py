# 这道题F12提示<!-- remember: 100*100 = (100+99+99+98) + (...  -->
# 下面是一张10000*1的原图 变成 100*100的形式
# 然后上面图片是一个圈饼
# 很明显了，答案让我们按圆圈的形状重构wire.png
# 解释：从(0,0)开始第一行向右走100步填充像素，然后剩下最外圈分别走了99,99,98步，一直走到中心……

import matplotlib.pyplot as plt
from PIL import Image

im = Image.open("src/wire.png") #这是oxygen.png黑白部分的位置
st = [] #记录走过的路径
def check(x,y):
    if x<0 or x> 99 or y<0 or y>99:
        return True
    if (x,y) in st:
        return True
    return False

def one_step(nx,ny,d):
    if d == 0:
        nx+=1
    elif d == 1:
        ny+=1
    elif d == 2:
        nx-=1
    elif d == 3:
        ny-=1
    return nx,ny

def reconstruct(pic):
    # 打开输入图片
    # 创建一个新的图片对象，与输入图片大小和模式相同
    out = Image.new(pic.mode, (100,100))
    nx = 0
    ny = 0
    d = 0
    cnt = 0
    for i in range(20000):
        if cnt >= 10000:
           break
        print(nx,ny,cnt,d)
        pixel = pic.getpixel((cnt, 0))
        out.putpixel((nx,ny),pixel)
        st.append((nx,ny))
        cnt += 1
        tmpx,tmpy = one_step(nx,ny,d)
        if check(tmpx,tmpy):
            d = (d+1)%4
        nx,ny = one_step(nx,ny,d)
    # 保存输出图片
    fig, ax = plt.subplots()
    ax.imshow(out)
    fig.savefig('src/wire_res.jpg')

# 调用函数重构图片，指定输入和输出路径
reconstruct(im)
plt.show()

# 发现图片是只猫，输入http://www.pythonchallenge.com/pc/return/cat.html
# 得到信息“and its name is uzi. you'll hear from him later.”
# 答案就是 http://www.pythonchallenge.com/pc/return/uzi.html
