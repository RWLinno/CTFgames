# 点开图片得到消息 a = [1, 11, 21, 1211, 111221,...
# len(a[30]) = ? 
# 直接在https://oeis.org/ 输入数列找到A005150
# 得到下面递推式，非常amazing

import itertools
x = "1"
for i in range(30):
    print(x)
    x = ''.join(str(len(list(g)))+k for k, g in itertools.groupby(x))

print(len(x))
# 答案是http://www.pythonchallenge.com/pc/return/5808.html

