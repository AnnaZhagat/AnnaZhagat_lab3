# TODO Напишите функцию для поиска индекса товара
def find_tovar(listt, tovar):
    index_item = 0
    for i in listt:
        if i == tovar:
            return index_item
        index_item+=1

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_tovar(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
