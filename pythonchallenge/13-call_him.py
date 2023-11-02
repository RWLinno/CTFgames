# 点开phonebook.php 发现打不开
# 想要了解一下php内部，所以先去学xmlrpc来返回内部方法
import xmlrpc.client as xc
url = "http://www.pythonchallenge.com/pc/phonebook.php"  # 将此处替换为你的 PHP 文件的 URL

if __name__ == '__main__':
    pp = xc.ServerProxy(url) 
    print (pp.system.listMethods())

# 输出结果 ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
# 看到了phone，让我们调用一下phone方法
    print (pp.phone('evil')) 
# 得到信息"He is not the evil"，算是成功了一大步
    print (pp.phone('Bert')) 
# 结合上一题的信息(上一题没用死活不理解，原来在下一关用了)，evil是Bert
# 得到答案555-ITALY (不知道555是什么意思)
# 彩蛋：输入ITALY.html会得到信息“SMALL letters.”

# 答案就是http://www.pythonchallenge.com/pc/return/italy.html