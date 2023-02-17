import json
from pyecharts.charts import Map
from pyecharts.options import *
f = open("疫情.txt", "r", encoding="UTF-8")
data = f.read()

data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
# 从字典得到省份数据
data_list = []
for province in province_data_list:
    province_name = province["name"]  # 省份名称
    province_name = province_name+"省"
    province_confirm = province["total"]["confirm"]  # 确诊人数
    data_list.append((province_name, province_confirm))
print(data_list)
map = Map()
map.add("确诊人数", data_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情", pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#FF9966"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#FF6666"},
            {"min": 100000, "max": 999999, "label": "100000-999999", "color": "#FF3333"},
            {"min": 1000000, "label": "1000000", "color": "#990033"}
        ]
    )
)
map.render("全国疫情地图.html")