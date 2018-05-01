import re, nltk

# present the options
print("======================================")
print("=========== WORD GENERATOR ===========")
print("======================================")
print("Please enter any number of letters and type 0 when you are finished.")

option_selected = False
letters = ''
while(not option_selected):

    option = input('Please enter some letters or enter 0 (on it\'s own) to quit: ')

    
    if re.findall("^\d+$", option):
        if int(option) == 0:
            option_selected = True
            break    
    if len(option) > 0:
        option = re.sub("[^a-zA-Z]", "", option)
        letters = letters + option

print("Letters selected are as follows: ", letters)
print(type(letters))
number_of_letters = len(letters)
print("======================================")
print("Please enter a number between 3 and", number_of_letters, "to generate words of that length from the letter list.")
print("======================================")
option_selected = False
length_of_word = 0
while(not option_selected):

    length_of_word = input(
        "Please enter some a number between 3 and " + str(number_of_letters) + ": ")

    try:
        length_of_word = int(length_of_word)
    except Exception as e:
        print("Please input a number above 3")
        continue
    
    if length_of_word >= 3 and length_of_word <= number_of_letters:
        option_selected = True
        break
puzzle_letters = nltk.FreqDist(letters)
wordlist = nltk.corpus.words.words()
word_list = [w for w in wordlist if len(w) == length_of_word and nltk.FreqDist(w) <= puzzle_letters]
print("============= WORD LIST ==============")
print(word_list)
print("======================================")
