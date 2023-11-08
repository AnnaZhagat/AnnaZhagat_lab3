# TODO Напишите функцию find_common_participants
def find_common_participants(l1, l2, sep_=','):
    a = set(l1.split("|"))
    b = set(l2.split("|"))
    l3 = list(set(a).intersection(b))
    return sorted(l3)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

com = find_common_participants(participants_first_group,participants_second_group)
print(com)
# TODO Провеьте работу функции с разделителем отличным от запятой


