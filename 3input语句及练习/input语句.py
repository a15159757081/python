print("请告诉我你是谁：")
name = input()
print("你好我叫", name)
print(type(name))
# 由此得知不管你输入什么数据类型，input都当做字符串数据类型看待

# 上面的代码整合为
name = input("请告诉我你是谁")
print(name)
# 得出结论input里面的字符串相当于print，和print做一样的工作输出

name = int(name)
print(type(name))
# 通过前面的学习得知我们可以使用int类型对前面的变量进行强转
