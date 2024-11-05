# TODO Напишите функцию find_common_participants

import re
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
f = "Иванов_Петров;Сидоров"
s = "Петров^Сидоров_Смирнов"

raz = "," # аргумент по умолчанию
print(f,"________", s)

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(f,s,raz = ","):
    new_f = re.split(r'[,.\n?!@|:;#$%^&*(){}_ ]+', f)
    new_s = re.split(r'[,.\n?!@|:;#$%^&*(){}_ ]+', s)
    common1 = [x for x in new_f if x in new_s]
    common1.sort()
    return common1

print(f,"________", s)
com = find_common_participants(f,s,raz)
print(com)
WER = raz.join(com)
print(WER)

