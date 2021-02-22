import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code:',r.status_code)

# 将API响应存储在一个变量中
reponse_dict = r.json()

# 处理结果
print(reponse_dict.keys())
print('Total repositories:', reponse_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = reponse_dict['items']
print('Repositories returned:',len(repo_dicts))

# 研究第一个仓库
first_repo_dict = repo_dicts[0]
print('\nkeys:',len(first_repo_dict))
for key in sorted(first_repo_dict.keys()):
    print(key)


names,stars,plot_dicts = [],[],[]
print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style = LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

# chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
chart = pygal.Bar(my_config,style = my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
# chart.add('',stars)
chart.add('',plot_dicts)
chart.render_to_file('17_use_api/python_repos.svg')