import json

f_us = open("美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
us_dict = json.loads(us_data)
trend_data = us_dict['data'][0]['trend']
trend_data = json.dumps(trend_data)
print(trend_data)