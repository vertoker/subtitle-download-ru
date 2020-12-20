from pytube import YouTube
import warnings
import os

warnings.filterwarnings("ignore")
link = input('Введите ссылку на видео: ')
caption = 'Субтитры отсутствуют'
yt = YouTube(link)

print(yt.captions.all())
try:
    caption_aru = yt.captions.get_by_language_code('a.ru')
    caption = caption_aru.generate_srt_captions()
    print('Русские авто-субтитры имеются')
except:
    print('Русские авто-субтитры отсутствуют')
try:
    caption_ru = yt.captions.get_by_language_code('ru')
    caption = caption_ru.generate_srt_captions()
    print('Русские субтитры имеются')
except:
    print('Русские субтитры отсутствуют')
print('\nСубтитры загружены')

result = yt.title + '\n'
counter = 1
for i in caption:
    if i == "\n":
        counter += 1
    if counter % 4 == 3:
        result += i
path = os.path.join(os.getcwd(), yt.title + '.txt')
open(path, 'w').write(result)
print('Субтитры записаны')
input('Нажмите Enter ')
