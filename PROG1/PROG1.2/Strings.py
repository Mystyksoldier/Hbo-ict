word1 = ("Supercalifragilisticexpialidocious")
word2 = ("Antidisestablishmentarianism")
word3 = ("Honorificabilitudinitatibus")
word_filter_question_2 = ("ice")
composer_list = ["Berlioz", "Borodin", "Brian", "Bartok", "Bellini", "Buxtehude", "Bernstein"]

answer_1 = len(word1)

result_word_2 = len(word2)
result_word_3 = len(word3)

result_question_4 = sorted(composer_list)

print("Vraag 1:")
print("De hoeveelheid nummers in het woord", word1, "is:", answer_1) 
print()

print("Vraag 2:")
if word_filter_question_2 in word1:
    print(word_filter_question_2, "komt in de tekst voor.")
else :
    print(word_filter_question_2, "komt niet in de tekst voor.")
print()

print("Vraag 3:")
if result_word_2 > result_word_3:
    print(word2, "is het langste woord.")
elif result_word_3 > result_word_2:
    print(word3, "is het langste woord.")
else:
    print("Bijde wooorden zijn even lang")
print()

print("Vraag 4:")
print(result_question_4[0])
print()

print("Vraag 5:")
print(result_question_4[-1])
