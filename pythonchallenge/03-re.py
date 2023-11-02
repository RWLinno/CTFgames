# 根据上一题一样，在文本中找出满足条件位置的字母就行了
# 1.中间为写字母，两边有且仅有3个大写字母
txt = ""
leng = 0
def check1(i): #检查两边大写字母
    if i<0 or i>=leng:
        return False
    if txt[i]<'A' or txt[i]>'Z':
        return False
    return True


def check2(i): #有且仅有3位，所以要再判一下边界
    if i<0 or i>=leng:
        return True
    if txt[i]>='A' and txt[i]<='Z':
        return False
    return True

with open("src/NNNxNNN.txt") as file:
    txt = file.read()
    leng = len(txt)
    for i in range(leng-3):
        if txt[i]>='a' and txt[i]<='z':
            if check1(i-1) and check1(i-2) and check1(i-3) and check1(i+1) and check1(i+2) and check1(i+3):
                if check2(i-4) and check2(i+4):
                    print(txt[i],end='')

# 得到了答案为 linkedlist
# 答案为：http://www.pythonchallenge.com/pc/def/linkedlist.php