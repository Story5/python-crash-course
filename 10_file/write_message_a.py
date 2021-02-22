# 这是一个文本存储器
print("这是一个文本存储器")
file = input("请输入文本路径:")
goon = True
while goon:
    s = input('\n请输入要存储的文本:')
    with open(file,'a') as file_object:
        file_object.write(s + "\n")
    goon_s = input('是否继续?y/n:\n')
    if goon_s == 'y':
        goon = True
    elif goon_s == 'n':
        goon = False