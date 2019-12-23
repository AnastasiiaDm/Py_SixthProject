s = '3. Дан текст состоящий из нескольких строк. \nВыведите слово, которое в этом тексте встречается чаще всего. \nЕсли таких слов несколько, выведите последнее. \nЕсли таких слов несколько, выведите последнее.'

text = {}

for word in s.split():
    if word in text:
        text[word] += 1
    else:
        text[word] = 1

max_cnt = 0
max_word = ''
for key, value in text.items():
    if value >= max_cnt:
        max_cnt = value
        max_word = key

print('Последнее чаще всего встречающееся слово: ', "\"", max_word, "\" - ", max_cnt, " раза", sep='')
