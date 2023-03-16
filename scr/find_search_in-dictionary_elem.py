# достает данные из файла в массив
# 6-ю строку менять в зависимости от разделителя
def from_file_in_list(file_name:str):
    a=[]
    with open(file_name, "r") as file:
        for line in file:
            line = line.split(", ")
            a.append(line)
    return a

# нахождение количества элементов в списке
# вернет словарь, где ключ=элемент, значение=количество
def dictionary_create(ls:list):
    dictionary = dict()
    for elem in set(ls):
        dictionary[elem] = ls.count(elem)
    return dictionary


