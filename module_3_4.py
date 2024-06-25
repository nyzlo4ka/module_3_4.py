def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in other_words:
        i = i.lower()
        if root_word in i or i in root_word:
            same_words.append(i)
    return same_words


v_1 = single_root_words('rIch', 'richiest', 'orichalcum', 'cheers', 'richies')
v_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(v_1)
print(v_2)

