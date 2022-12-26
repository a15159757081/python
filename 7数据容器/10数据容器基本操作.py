my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

print(f"列表元素的个数有{len(my_list)}")
print(f"元组元素的个数有{len(my_tuple)}")
print(f"字符串元素的个数有{len(my_str)}")
print(f"集合元素的个数有{len(my_set)}")
print(f"字典元素的个数有{len(my_dict)}")

print(f"列表元素的最大值有{max(my_list)}")
print(f"元组元素的最大值有{max(my_tuple)}")
print(f"字符串元素的最大值有{max(my_str)}")
print(f"集合元素的最大值有{max(my_set)}")
print(f"字典元素的最大值有{max(my_dict)}")

print(f"列表元素的最小值有{min(my_list)}")
print(f"元组元素的最小值有{min(my_tuple)}")
print(f"字符串元素最小值有{min(my_str)}")
print(f"集合元素的最小值有{min(my_set)}")
print(f"字典元素的最小值有{min(my_dict)}")

print(f"列表转列表的结果是{list(my_list)}")
print(f"元组转列表的结果是{list(my_tuple)}")
print(f"字符串转列表的结果是{list(my_str)}")
print(f"集合转列表的结果是{list(my_set)}")
print(f"字典转列表的结果是{list(my_dict)}")

print(f"列表转元组的结果是{tuple(my_list)}")
print(f"元组转元组的结果是{tuple(my_tuple)}")
print(f"字符串转元组的结果是{tuple(my_str)}")
print(f"集合转元组的结果是{tuple(my_set)}")
print(f"字典转元组的结果是{tuple(my_dict)}")

print(f"列表转列表的结果是{list(my_list)}")
print(f"元组转列表的结果是{list(my_tuple)}")
print(f"字符串转列表的结果是{list(my_str)}")
print(f"集合转列表的结果是{list(my_set)}")
print(f"字典转列表的结果是{list(my_dict)}")

print(f"列表转字符串的结果是{str(my_list)}")
print(f"元组转字符串的结果是{str(my_tuple)}")
print(f"字符串转字符串的结果是{str(my_str)}")
print(f"集合转字符串的结果是{str(my_set)}")
print(f"字典转字符串的结果是{str(my_dict)}")

print(f"列表转集合的结果是{set(my_list)}")
print(f"元组转集合的结果是{set(my_tuple)}")
print(f"字符转集合的结果是{set(my_str)}")
print(f"集合转集合的结果是{set(my_set)}")
print(f"字典转集合的结果是{set(my_dict)}")

# 容器的排序(排序之后自动变为列表元素，并且字典转列表会丢失value)
my_list = [3, 2, 1, 5, 4]
my_tuple = (1, 3, 2, 5, 4)
my_str = "abcdefg"
my_set = {2, 1, 4, 5, 3}
my_dict = {"key2": 2, "key3": 3, "key1": 1, "key4": 4, "key5": 5}
print(f"列表对象的排序结果；{sorted(my_list)}")
print(f"元组对象的排序结果；{sorted(my_tuple)}")
print(f"字符串对象的排序结果；{sorted(my_str)}")
print(f"集合对象的排序结果；{sorted(my_set)}")
print(f"字典对象的排序结果；{sorted(my_dict)}")