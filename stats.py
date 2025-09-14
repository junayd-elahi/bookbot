def get_num_words(text):
    words = text.split()
    return len(words)

def count_words(text):
    words = text.split()
    letters = {}
    for word in words:
        lowered = word.lower()
        for letter in lowered:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def sort_helper(item):
   return item["num"]

def sort_characters(letters):
    sorted_count_words = []
    for key,value in letters.items():
            sorted_count_words.append({"char":key,"num":value})
    sorted_count_words.sort(key=sort_helper,reverse=True)
    return sorted_count_words





