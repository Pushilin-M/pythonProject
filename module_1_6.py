my_dict = {'Manya': 2012 , 'Vlad': 1998 , 'Kolyan':2020 }
print(my_dict)
print(my_dict['Vlad'],my_dict.get('Alex'))
my_dict.update({'Sergey': 2015 , 'Yuriy': 1983})
a = my_dict.pop('Manya')
print(a)
print(my_dict)

my_set = {1,4,6,0.3,0.7,4,1,0.3}
my_set.add('Element')
my_set.add(False)
my_set.discard(0.7)
print(my_set)