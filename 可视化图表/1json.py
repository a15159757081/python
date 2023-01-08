"""
json是一种轻量级交互格式，可以按照json指定格式去组织合封装数据
json本质上是一个带有特定格式的字符串
"""
import json

# 准备一个列表，列表的每一个元素都是字典
data = [{"name": "薛之谦", "age": "13"}, {"name": "周杰伦", "age": "20"}, {"name": "邓紫棋", "age": "18"}]
json_str = json.dumps(data, ensure_ascii=False)  # 不使用ASCII码转换
print(f"内容为{json_str},数据类型为{type(json_str)}")
d = {"name": "周杰伦", "add": "台北"}
json_str = json.dumps(d, ensure_ascii=False)  # 不使用ASCII码转换
print(f"内容为{d},数据类型为{type(d)}")