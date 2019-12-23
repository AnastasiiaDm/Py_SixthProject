s = '1. В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте тексте .'

words = {}

for word in s.split():
    # if word in words:
    #     words[word] += 1
    # else:
    #     words[word] = 1

    words[word] = words.get(word, 0) + 1

print(words)