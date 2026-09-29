file = open("sandbox/notes.txt", "w", encoding="utf-8")
file.write("Первая строка что же сюда написать\n")
file.write("Первая строка Вопросов еще больше \n")
file.close()

file = open("sandbox/notes.txt", "a", encoding="utf-8")
file.write("третья строка: не перезаписываем, а дополняем то, что уже есть")

file = open("sandbox/notes.txt", "r", encoding="utf-8")
text = file.read()
file.close()

print(text)
print(f"Количество символов: {len(text)}")


print("Hello world")