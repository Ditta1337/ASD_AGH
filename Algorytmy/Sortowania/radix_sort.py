def sort_word(word):
    k = ord("z") - ord("a") + 1 # REMEMBER + 1
    n = len(word)
    ret = ""
    C = [0] * k
    B = [0] * n

    for letter in word:
        C[ord(letter) - ord("a")] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for j in range(n-1, -1, -1):
        B[C[ord(word[j]) - ord("a")] - 1] = word[j]
        C[ord(word[j]) - ord("a")] -= 1
    
    for i in range(n):
        ret += B[i]
    
    return ret

def sort_words_pos(words, pos):
    k = ord("z") - ord("`") + 1
    n = len(words)
    C = [0] * k
    B = [0] * n

    for word in words:
        C[ord(word[pos]) - ord("`")] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for j in range(n-1, -1, -1):
        B[C[ord(words[j][pos]) - ord("`")] - 1] = words[j]
        C[ord(words[j][pos]) - ord("`")] -= 1

    for i in range(n):
        words[i] = B[i]

def radix_sort(words):
    max_length_word = max(len(word) for word in words)
    for i in range(len(words)):
        words[i] += "`" * (max_length_word - len(words[i]))
    print(words)
    for pos in range(max_length_word - 1, -1, -1):
        sort_words_pos(words, pos)

    for i in range(len(words)):
        words[i] = words[i].split("`")[0]


words = ["abcd", "fsdf", "cbda", "fa", "artur"]

new = []
for word in words:
    new.append(sort_word(word))

print(new)
radix_sort(new)
print(new)
print(chr(ord("a") - 1))

