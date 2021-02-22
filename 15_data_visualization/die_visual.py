from die import Die
import pygal

die = Die()


count = 1000
results = []
for roll_num in range(count):
    result = die.roll()
    results.append(result)

# print(results)

#分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

#对结果进行可视化
hist = pygal.Bar()
hist.title = 'Result of rolling one D6 ' + str(count) + ' times.'
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6',frequencies)
hist.render_to_file('15_data_visualization/die.visual.svg')

