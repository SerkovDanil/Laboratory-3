main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO  Напишите функцию count_letters
def count_letters(text):
    result = {}
    for letter in text:
        if letter.isalpha():
            if letter not in result:
                result[letter.lower()] = 1
            else:
                result[letter.lower()] += 1
    return result


# TODO Напишите функцию calculate_frequency
def calculate_frequency(result):
    number_letters = 0
    for cer in result:
        number_letters += result[cer]
    share = {}
    for cer in result:
        share[cer] = result[cer] / number_letters
    return share 


# TODO Распечатайте в столбик букву и её частоту в тексте


letter_share  = calculate_frequency(count_letters(main_str))
for cer in letter_share :
    print(f"{cer}:", "%.2f" % letter_share[cer])