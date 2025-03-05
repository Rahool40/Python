# Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.” as a single string.
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Reprint this sentence as “The quick brown fox jumps over the lazy dog.” using the replace() function to replace every “!” exclamation mark with a blank space.
rep_sentence = sentence.replace("!" ,  " ")
print(rep_sentence)

# Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.” using the upper() function
up_sentence = rep_sentence.upper()
print(up_sentence)

# Reprint the sentence in reverse
print(sentence[::-1])