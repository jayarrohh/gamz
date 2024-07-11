import csv

with open("DirtyWords.csv", newline="") as f:
    reader = csv.reader(f)
    banned_words = list(reader)

banned_cut = []

# Removes first and last item in each nested list
for nested in banned_words:
    banned_cut.append(nested[1])


with open("GuessWords.csv", newline="") as f:
    reader = csv.reader(f)
    words_orig = list(reader)

wordie_words = []

for nested in words_orig:
    wordie_words.append(nested[0])
    
print(wordie_words)