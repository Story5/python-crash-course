filepath = '10_file'
filename = 'programming'
fileformat = 'txt'
with open(filepath + "/" + filename + "." + fileformat, 'w') as file_object:
    # print('here')
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.")

# Python 只能将字符串写入文本文件中.要将数值数据存储到文本文件中,必须先使用函数str()将其转换为字符串格式