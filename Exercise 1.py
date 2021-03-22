# Q. Create a dictionary and take input from the user. Then return the meaning of the word from the dictionary

dict1 = {"abject": "of the most contemptible kind",
         "aberration": "a state or condition markedly different from the norm",
         "abjure": "formally reject or disavow a formerly held belief",
         "abnegation": "the denial and rejection of a doctrine or belief",
         "abrogate": "revoke formally"}
input_word = input('Type the word you want to know meaning of\n')
if input_word in dict1:
    print(dict1[input_word])
else:
    print("This word is not in this dictionary")
