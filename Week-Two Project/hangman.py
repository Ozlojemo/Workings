
import random

words=["lengths","lucky", "luxury", "lymph", "subway", "swivel"]

#Add a functioon that randomly selects one word from the list
def select_words(words):
    return random.choice(words)

#Call the function just for test
print(select_words(words))