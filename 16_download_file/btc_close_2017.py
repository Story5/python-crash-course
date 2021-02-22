from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import json
import pygal
import math
from itertools import groupby

json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
filepath = '16_download_file'


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(filepath+'/'+title+'.svg')
    return line_chart


try:
    import requests
except ModuleNotFoundError:
    try:
        # Python 2.x 版本
        from urllib2 import urlopen
    except ImportError:
        # Python 3.x 版本
        from urllib.request import urlopen

    response = urlopen(json_url)
    req = response.read()

    urlopen_filename = filepath + '/btc_close_2017_urllib.json'
    with open(urlopen_filename, 'wb') as f:
        f.write(req)

    file_urllib = json.loads(req)
    # print(file_urllib)
else:
    req = requests.get(json_url)

    request_filename = filepath + '/btc_close_2017_request.json'
    with open(request_filename, 'w') as f:
        f.write(req.text)

    file_requests = req.json()
    print(file_requests)


dates = []
months = []
weeks = []
weekdays = []
closees = []

filename = '16_download_file/btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
for btc_dict in btc_data:
    date = btc_dict['date']
    dates.append(date)

    month = btc_dict['month']
    months.append(month)

    week = btc_dict['week']
    weeks.append(week)

    weekday = btc_dict['weekday']
    weekdays.append(weekday)

    close = int(float(btc_dict['close']))
    closees.append(close)
    print('{} is month {} week {}, {}, the close price is {} RMB'.format(
        date, month, week, weekday, close))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价(¥)'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in closees]
line_chart.add('收盘价', closees)
line_chart.render_to_file(filepath + '/收盘价折线图(¥).svg')

# line_chart.add('log收盘价',close_log)
# line_chart.render_to_file(filepath + '/log收盘价折线图(¥).svg')
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(
    months[:idx_month], closees[:idx_month], '收盘价月日均值(¥)', '月日均值')
line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(
    weeks[1:idx_week], closees[1:idx_week], '收盘价周日均值(¥)', '周日均值')
line_chart_week

wd = ['Monday', 'Tuesday', 'Wednesday',
      'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
try:
    line_chart_weekday = draw_line(
    weekdays_int, closees[1:idx_week], '收盘价星期均值(¥)', '星期均值')
except TypeError:
    pass
else:
    line_chart_weekday.x_labels = wd
    line_chart_weekday.render_to_file('收盘价星期均值(¥).svg')


with open(filepath + '/收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            '收盘价折线图（¥）.svg', '收盘价对数变换折线图（¥）.svg', '收盘价月日均值（¥）.svg',
            '收盘价周日均值（¥）.svg', '收盘价星期均值（¥）.svg'
    ]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))  # 1
    html_file.write('</body></html>')