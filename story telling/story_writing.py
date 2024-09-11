with open('story telling/story.txt','r') as f:
    story = f.read()
    # print(story)

start_word = -1
words = set()

target_start = '<'
target_end = '>'

for i,char in enumerate(story):
    if char == target_start:
        start_word = i

    if char == target_end and start_word != -1:
        word = story[start_word:i+1]
        words.add(word)
        start_word = -1
    
# print(words)

answers = {}

for word in words:
    ans = input('give the word for '+word+'.')
    answers[word] = ans
    story = story.replace(word,answers[word])

print(story)



