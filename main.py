from pytube import YouTube
import warnings
import os

def Time(time):
    result = 0
    hours = int(time[0:2])
    minutes = int(time[3:5])
    seconds = int(time[6:8])
    meleeseconds = int(time[9:12])
    return hours * 3600 + minutes * 60 + seconds + meleeseconds / 1000

def TextFormater(caption):
    result = yt.title + '\n'
    timeStart = Time("00:00:00,000")
    timeEnd = Time("00:00:00,000")
    isParagraph = False
    inBracket = False
    counter = 0
    line = ''
    for i in caption:
        if i != "\n":
            #if i == '[':
                #inBracket = True
            
            if not inBracket:
                line += i
            
            #if i == ']':
                #inBracket = False
        else:
            counter += 1
            if counter % 4 == 2:
                timeStartLocal = Time(line[:12])
                timeEndLocal = Time(line[-12:])
                isParagraph = timeEnd < timeStartLocal
                timeStart = timeStartLocal
                timeEnd = timeEndLocal
            if counter % 4 == 3:
                result += line
                if isParagraph == True:
                    result += "\n"
                else:
                    result += " "
            line = ''
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
    open(path2, 'w').write(result)
    print('Субтитры записаны')
input('Нажмите Enter ')
