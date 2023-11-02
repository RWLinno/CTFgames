# F12 有提示一个链接是href="linkedlist.php?nothing=12345"
# 点进去提示and the next nothing is 44827，发现是下一个页面
# 我们来写一个脚本依次跳转页面，改变nothing参数即可。

import re
import requests

nothing = '63579' #12345 -> 8022 -> 63579
cnt = 141 #1-> 86 -> 141

response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing)

while True:
    response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing)
    txt = response.text
    nxt = re.findall(r'\d+',txt)
    if len(nxt) > 0:
        nxt = nxt[0]
    else:
        break
    print("context:",txt,"now",nothing,"next:",nxt,"count:",cnt)
    cnt += 1
    nothing = nxt

# 第一次在16044断了，但是无所谓，进到16044告诉我们除2再跑
# 把nothing改成8022继续!
# 再跑一次告诉我们从nothing=63579再跑
# 程序在66831停下了，输入进去发现了答案 -> peak.html