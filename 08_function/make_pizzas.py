# import pizza
# pizza.make_pizza(16,"pepperoni")
# pizza.make_pizza(12,"mushrooms", "green pepers", "extra cheese")

# 使用as给模块制定别名
# import pizza as p
# p.make_pizza(16,"pepperoni")
# p.make_pizza(12,"mushrooms", "green pepers", "extra cheese")

# 导入特定的函数
# from pizza import make_pizza
# make_pizza(16,"pepperoni")
# make_pizza(12,"mushrooms", "green pepers", "extra cheese")

# 使用as给函数制定别名
# from pizza import make_pizza as mp
# mp(16,"pepperoni")
# mp(12,"mushrooms", "green pepers", "extra cheese")

# 导入模块中所有函数
from pizza import *
make_pizza(16,"pepperoni")
make_pizza(12,"mushrooms", "green pepers", "extra cheese")