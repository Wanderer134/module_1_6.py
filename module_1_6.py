my_dict = {'Denis': 123455, 'Anna': 3457634, 'Max': 48458}
print(my_dict)
print(my_dict['Anna'])
print (my_dict.get('Masha'))
my_dict.update({'Nikita': 656256, 'Larisa': 6256354})
a = my_dict.pop('Denis')
print(a)
print(my_dict)

my_set = {1, 1, 4, 4, 'apple', 'apple',False}
print(set(my_set))
my_set.add(6)
my_set.add('banana')
my_set.remove(1)
print(my_set)
