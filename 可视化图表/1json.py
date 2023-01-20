"""
json是一种轻量级交互格式，可以按照json指定格式去组织合封装数据
json本质上是一个带有特定格式的字符串
"""
import json

# 准备一个列表，内部嵌套列表，列表里面存放字典
data = [{"name": "薛之谦", "age": "13"}, {"name": "周杰伦", "age": "20"}, {"name": "邓紫棋", "age": "18"}]
json_str = json.dumps(data, ensure_ascii=False)  # 不使用ASCII码转换
print(f"内容为{json_str},数据类型为{type(json_str)}")

# 单纯使用列表内部元素为字典
d = {"name": "周杰伦", "add": "台北"}
json_str = json.dumps(d, ensure_ascii=False)  # 不使用ASCII码转换
print(f"内容为{d},数据类型为{type(d)}")

# 讲json字符串转换为python数据类型[{k:v,k:v},{k:v,k:v}]
s = '[{"name": "薛之谦", "age": "13"}, {"name": "周杰伦", "age": "20"}, {"name": "邓紫棋", "age": "18"}]'
# 注意最外面的单引号s存储的必须为字符串
l = json.loads(s)
print(type(l))  # 转换得到列表数据类型

# 讲json字符串转换为python数据类型{k:v,k:v}
s = '{"name": "周杰伦", "add": "台北"}'
l = json.loads(s)
print(type(l))