def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params (2,  25, [1, 2, 3]) #срабатывает, если задать еще а
values_list = ['In', 45, [2, 4, 7]]
values_dict = {'a': 'MOM', 'b': '0802', 'c': '0803'}
print_params(*values_list) # распаковка списка
print_params(**values_dict) #распаковка словаря
values_list_2 = [43, 'MIO'] # новый список с двумя параметрами
print_params(*values_list_2, 42) # работает
