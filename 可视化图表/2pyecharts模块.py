from pyecharts.charts import Line

Line = Line()
Line.add_xaxis(["中国", "美国", "英国"])
Line.add_yaxis("GDP", [20, 30, 20])
Line.render()