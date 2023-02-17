from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
# 获取地图对象
data = [
    ("北京市", 9),
    ("上海市", 19),
    ("湖南省", 199),
    ("福建省", 299),
    ("台湾省", 399)
]
# 列表内部嵌套元组的数据类型格式
map.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True, is_piecewise=True, pieces=[
        {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},  #
        {"min": 10, "max": 99, "label": "10-99", "color": "#CC6666"},
        {"min": 100, "max": 999, "label": "10-999", "color": "#990033"}
    ])

)
map.add("地图", data, "china")  # 数据添加到地图对象
map.render()