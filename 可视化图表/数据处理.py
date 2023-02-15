import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, VisualMapOpts

f_us = open("美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()

f_jp = open("日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()

f_in = open("印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()

# 去掉不合理开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 去掉不合理结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# json转字典格式
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取到日期数据，用于x轴，获取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确认数据,用于y轴，下标到314
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图标
line = Line()  # 拿到折线图数据

line.add_xaxis(us_x_data)  # x轴是供用的
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))  # label去除折线图文字
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置标题
line.set_global_opts(
    title_opts=TitleOpts(title="2020确诊人数", pos_left="center", pos_bottom="1%")
)
line.render()
f_us.close()
f_jp.close()
f_in.close()
