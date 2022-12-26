my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
# 新增元素
my_dict["张信哲"] = 66
print(f"字典结果新增元素后{my_dict}")

# 更新元素
my_dict["周杰伦"] = 33
print(f"字典经过更新后{my_dict}")

# 删除元素
score = my_dict.pop("周杰伦")
print(f"字典中被移除元素后为{my_dict}, 移除后的元素{score}")

# 清空元素
my_dict.clear()
print(f"字典内容清空后内容{my_dict}")

# 获取全部key
my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
keys = my_dict.keys()
print(f"字典的全部key是{keys}")

# 遍历字典
# 方法一通过获取全部的key来遍历
for key in keys:
    print(f"字典的key是{key}")
    print(f"字典的value为{my_dict[key]}")

# 方式二直接对字典进行for循环每次都能得到key
for key in my_dict:
    print(f"2字典的key是{key}")
    print(f"字典的value为{my_dict[key]}")

# 字典不支持下标索引索引不支持while循环

# 统计字典的元素数量
num = len(my_dict)
print(f"字典中的元素数量是{num}")

# 练习
gzb = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1},
    "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2},
    "林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3},
    "张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1},
    "刘德华": {
        "部门": "市场部",
        "工资": 3000,
        "级别": 2}}
print(gzb)
for i in gzb:  # i这里获取到的是字典的key值那么我们要进入嵌套首先就要进入第一个字典的第一个key
    if gzb[i]["级别"] == 1:
        gzb[i]["级别"] += 1
        gzb[i]["工资"] += 1000
print(gzb)
