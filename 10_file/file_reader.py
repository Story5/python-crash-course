# with open('10_file/pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

filepath = '10_file'
filename = 'pi_digits'
m_filename = 'pi_million_digits'
fileformat = 'txt'

with open(filepath+"/"+filename + "."+fileformat) as file_object:
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

with open(filepath + "/" + m_filename + "." + fileformat) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(len(pi_string))
print(pi_string[:52] + "...")

goon = True
while (goon):
    s_bri = input('Enter your birthday:\n')
    if s_bri in pi_string:
        print('yes')
    else:
        print('no')
    goon_string = input('Go on or not,input y/n:\n')
    if (goon_string.lower() == 'y'):
        goon = True
    elif (goon_string.lower() == 'n'):
        goon = False