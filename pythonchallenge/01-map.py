# 图片中每个字母都向后移动了两位，也就叫我们用凯撒加密处理下面的文字

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for i in str:
    if i >= 'a' and i <= 'x':
        print(chr(ord(i)+2),end='')
    elif i>'x':
        print(chr(ord(i)+2-26),end='')
    else:
        print(i,end='')


# 得到i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
# 我们把url中的‘map’做相应操作得到 -> ocr
# 答案就是 http://www.pythonchallenge.com/pc/def/ocr.html

