message_1 = "This is a string";
message_2 = 'This is also a string';
# 首字母大写
print(message_1.title());
# 大写
print(message_1.upper());
# 小写
print(message_1.lower());

first_name = "ada";
last_name = "lovelace";
full_name = first_name + " " + last_name;
print(full_name);

print("\tPython");
print("Language:\nPython\nC\nJavaScript");
print("Language:\n\tPython\n\tC\n\tJavaScript");

favorite_language = "python ";
print(len(favorite_language));
print(favorite_language.rstrip());
print(favorite_language);

favorite_language = " python ";
print(len(favorite_language));
# 删除末尾空格
print(favorite_language.rstrip());
# 删除开头空格
print(favorite_language.lstrip());
# 删除两端空格
print(favorite_language.strip());
