"""
09. Стохастические тексты — Тео Лутц, 1959.

Первые компьютерные стихи: программа на Zuse Z22 случайно соединяла слова
по грамматической схеме «оператор + подлежащее + сказуемое». Это русская
версия программы Ника Монтфорта «Stochastic Texts» (2014, 2024), словарь
подобран заново.

В русском языке слово «каждый» и прилагательное согласуются с существительным
в роде, поэтому у каждого существительного записан род, а у каждого
прилагательного и оператора — три формы.

Copyright (c) 2014, 2024 Nick Montfort <nickm@nickm.com>, inspired by a 1959
program by Theo Lutz. Copying and distribution of this file, with or without
modification, are permitted in any medium without royalty provided the
copyright notice and this notice are preserved. This file is offered as-is,
without any warranty.
"""
from random import choice
from time import sleep

# род: 0 — мужской, 1 — женский, 2 — средний
subjects = {"оля": 1, "тигр": 0, "зебра": 1, "лев": 0,
            "жаба": 1, "крыса": 1, "паук": 0, "таракан": 0,
            "муха": 1, "стрекоза": 1, "мышь": 1, "полина": 1,
            "киска": 1, "нина": 1, "жук": 0, "пингвин": 0}

# формы: (мужской, женский, средний)
predicates = [("хитрый", "хитрая", "хитрое"),
              ("милый", "милая", "милое"),
              ("ласковый", "ласковая", "ласковоеое"),
              ("подозрительный", "подозрительная", "подозрительное"),
              ("толстый", "толстая", "столстоеое"),
              ("кислый", "кислая", "кислое"),
              ("мощный", "мощная", "мощное"),
              ("влюбленный", "влюбленная", "влюбленное"),
              ("жадный", "жадная", "жадное"),
              ]

# запятая нужна: «и», «или», «поэтому» соединяют два предложения
conjunctions = [", и ", ", или ", ", поэтому ", ". ", ". ", ". ", ". ", ". "]

# формы: (мужской, женский, средний)
operators = [("этот", "эта", "это"),
             ("каждый", "каждая", "каждое"),
             ("ни один", "ни одна", "ни одно"),
             ("не каждый", "не каждая", "не каждое")]

def element():
    subject = choice(list(subjects))
    gender = subjects[subject]
    operator = choice(operators)[gender]
    predicate = choice(predicates)[gender]
    if operator.startswith("ни"):    # «ни один» требует «не»
        predicate = "не " + predicate
    text = operator + " " + subject + " " + predicate
    return text[0].upper() + text[1:]          # первая буква — заглавная

def line():
    first = element()
    conjunction = choice(conjunctions)
    second = element()
    if not conjunction == ". ":
        second = second.lower()
    return first + conjunction + second + ".\n"

print()
while True:
    print(line())
    sleep(4.0)
