def alphabet_buckets(words, index=0):
    if not words:
        return []

    buckets = {chr(letter): [] for letter in range(ord('a'), ord('z') + 1)}

    result = []
    for word in words:
        if len(word) > index:
            buckets[word[index].lower()].append(word)
        elif len(word) == index:
            result.append(word)

    for letter in buckets:
        if buckets[letter]:
            result += alphabet_buckets(buckets[letter], index + 1)

    return result


# Example usage
words = ['a', 'b', 'ab']
sorted_words = alphabet_buckets(words)
print(sorted_words)