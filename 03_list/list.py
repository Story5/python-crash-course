bicycles = ['trek','cannondale','redline','specialized'];
print(bicycles);
print(bicycles[0]);

bicycles[0] = "dacati";
print(bicycles);

bicycles.append("ducati");
print(bicycles);

bicycles.insert(0,"ducati");
print(bicycles);

del bicycles[0];
print(bicycles);

bicycles.pop();
print(bicycles);

bicycles.pop(0);
print(bicycles);


bicycles.remove('redline');
print(bicycles);

# 排序
cars = ['bmw','audi',"toyota",'subaru'];
cars.sort();
print(cars);
cars.sort(reverse=True);
print(cars);


cars = ['bmw','audi',"toyota",'subaru'];
print("Here is the original list:");
print(cars);
print("\nHere is the sorted list:");
print(sorted(cars));
print("\nHere is the original list:");
print(cars);

cars.reverse();
print(cars);

print(len(cars));