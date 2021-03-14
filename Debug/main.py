from pytube import YouTube
import warnings
import os

def ReplaceLetter(string, letter, index):
    return "".join((string[:index], letter, string[index + 1:]))

def Time(time):
    result = 0
    hours = int(time[0:2])
    minutes = int(time[3:5])
    seconds = int(time[6:8])
    meleeseconds = int(time[9:12])
    return hours * 3600 + minutes * 60 + seconds + meleeseconds / 1000

def TextFormater(caption):
    result = yt.title + '\n'
    
    startTimings = []
    endTimings = []
    lines = []
    
    counter = 0
    line = ''
    for i in caption:
        if i != "\n":
            line += i
        else:
            counter += 1
            if counter % 4 == 2:
                startTimings.append(Time(line[:12]))
                endTimings.append(Time(line[-12:]))
            if counter % 4 == 3:
                if line[0] == '[' or line[-1] == ']':
                    startTimings.pop()
                    endTimings.pop()
                else:
                    lines.append(line)
            line = ''
    
    lines[0] = ReplaceLetter(lines[0], lines[0][0].upper(), 0) + ' '
    for i in range(1, len(lines) - 1):
        isParagraph = endTimings[i - 1] < startTimings[i]
        if isParagraph:
            if lines[i-1][-1] == ' ':
                lines[i-1] = lines[i-1][:-1] + '.\n'
            else:
                lines[i-1] += '.\n'
            lines[i] = ReplaceLetter(lines[i], lines[i][0].upper(), 0) + ' '
        else:
            lines[i] = lines[i] + ' '
    
    isParagraph = endTimings[-2] < startTimings[-1]
    if isParagraph:
        if lines[-1][-1] == ' ':
            lines[-1] = lines[-2][:-1] + '.\n'
        else:
            lines[-1] += '.\n'
        lines[-1] = ReplaceLetter(lines[-1], lines[-1][0].upper(), 0) + ' '
    else:
        lines[-1] = lines[-1] + ' '

    for i in range(len(lines)):
        result += lines[i]
    
    return result

warnings.filterwarnings("ignore")
link = input('Введите ссылку на видео: ')
caption = 'Субтитры отсутствуют'
yt = YouTube(link)

name = yt.title
block_list = ["\\", "/", ":", "*", "?", "<", ">", "|"]
for char in block_list:
    name = name.replace(char, '')
print(yt.captions.all())

#Английские авто-субтитры
try:
    caption_aen = yt.captions.get_by_language_code('a.en')
    caption = caption_aen.generate_srt_captions()
    print('Английские авто-субтитры имеются')
except:
    print('Английские авто-субтитры отсутствуют')
#Английские субтитры
try:
    caption_en = yt.captions.get_by_language_code('en')
    caption = caption_en.generate_srt_captions()
    print('Английские субтитры имеются')
except:
    print('Английские субтитры отсутствуют')
#Русские авто-субтитры
try:
    caption_aru = yt.captions.get_by_language_code('a.ru')
    caption = caption_aru.generate_srt_captions()
    print('Русские авто-субтитры имеются')
except:
    print('Русские авто-субтитры отсутствуют')
#Русские субтитры
try:
    caption_ru = yt.captions.get_by_language_code('ru')
    caption = caption_ru.generate_srt_captions()
    print('Русские субтитры имеются')
except:
    print('Русские субтитры отсутствуют')
print('\nСубтитры загружены')

if caption != 'Субтитры отсутствуют':
    result = TextFormater(caption)
    path = os.path.join(os.getcwd(), name + '.txt')
    path2 = os.path.join('C:\\Users\\The Witcher\\Desktop', name + '.txt')
    path3 = os.path.join('C:\\Users\Eduard\\OneDrive\\Рабочий стол', name + '.txt')
    open(path3, 'w').write(result)
    print('Субтитры записаны')
input('Нажмите Enter ')
