import pymorphy2
import pymorphy2_dicts_ru
import pymorphy2_dicts_uk
import re

morph = pymorphy2.MorphAnalyzer()

'''
gr = morph.parse("блестящий")  #морфологический разбор слова
print(gr)
for i in range(len(gr)):
    print(' ******2****** ', '\n Тэг - ', gr[i].tag, "\n Часть речи -", gr[i].tag.POS, '\n нормальная форма - ', gr[i].normal_form, '\n тэг кириллицей - ', gr[i].tag.cyr_repr, '\n вероятностная оценка - ', gr[i].score)


adj=morph.parse("блестящий")[0]   #морфологический разбор прилагательного
prtf=morph.parse("блестящий")[2]  #морфологический разбор причастия
print(' ******3****** ', '\n падеж - ', adj.tag.case, '\n род - ', adj.tag.gender, '\n число - ', adj.tag.number, '\n совершенный и несовершенный вид - ', adj.tag.aspect, '\n переходность - ', adj.tag.transitivity,
      '\n творительный падеж', adj.inflect({'ablt'}), '\n творительный падеж, множественное число', morph.parse('блестящими'), '\n лексема слова прилагательного', adj.lexeme, '\n лексема слова причастия', prtf.lexeme)
'''

f1 = open(r'D:\PycharmProjects\project\Pymorphy\russian.txt', 'r', encoding='utf8')
f2 = open(r'D:\PycharmProjects\project\Pymorphy\tags.txt', 'w', encoding='utf8')
t = f1.read().lower()
pattern = re.compile(r"\w{3,}|\w{2,}-\w{2,}")
list = pattern.findall(t)
for i in range(len(list)):
    parsed = morph.parse(list[i])
    for j in range(len(parsed)):
        print('')
    f2.write(list[i] + " - " + parsed[j].tag.POS + '\n')
f1.close()
f2.close()
