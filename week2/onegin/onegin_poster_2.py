from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 4320, 7680
MARGIN = 260 #отступы
LINE_HEIGHT = 21
FONT = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 16)

with open("data/onegin.txt", encoding="utf-8") as file:
    words = file.read().split()

print(f"Кол-во слов: {len(words)}")

lines = []
line = words[0]

for word in words[1:]:
    longer = line + " " + word
    if FONT.getlength(longer) <= WIDTH - 2 * MARGIN:
        line = longer
    else:
        lines.append(line)
        line = word    

lines.append(line)
print(f"кол-во строк на изображении: {len(lines)}")

image = Image.new("RGB", (WIDTH, HEIGHT), "#FFFFFF")
#################
evgenys = []
olgas =[]
############3#
draw = ImageDraw.Draw(image)
y = MARGIN

for line in lines:
    draw.text((MARGIN, y), line, font=FONT, fill="#3C3A34")
    ##############
    x = MARGIN
    for word in line.split(" "):
        if"Евген" in word or "Онеги" in word:
            evgenys.append((x, y + LINE_HEIGHT))
        if "Ольг" in word:
            olgas.append((x, y + LINE_HEIGHT))
        x += FONT.getlength(word + " ")
    ##############
    y = y + LINE_HEIGHT

###########
print(f"Кол-во Евгениев: {len(evgenys)}. Кол-во Ольг: {len(olgas)}")

pen = ImageDraw.Draw(image, "RGBA")
for evgeny in evgenys:
    for olga in olgas:
        pen.line([evgeny, olga], fill=(255, 255, 255, 100), width=3)
#########
image.save("onegin_poster.png")
print("ВСЁ ГОТОВО!!!")


    

print("Hello world")