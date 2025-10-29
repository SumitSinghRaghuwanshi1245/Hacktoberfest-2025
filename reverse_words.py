def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

s = input("Enter a sentence: ")
print("Original:", s)
print("Reversed (words):", reverse_words(s))
