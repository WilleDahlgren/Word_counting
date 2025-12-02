
#takes in a list of strings and tokenizes it
def tokenize(lines):  
    words = []
    for line in lines:
        line = line.lower()
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start += 1
            end = start
            if end < len(line): #If we have a list with only spaces it makes no sense to continue testing because the value of end exceeds the number of elements.
                if line[end].isalpha():
                    while end < len(line) and line[end].isalpha(): #checks if the current character is a letter. At the end of this loop end will be 1 larger than "necessary" because the slice notation only picks upp the letters start to end-1.
                        end += 1                                   #If it is, add end by one. If a word is 4 letters start has to be 0 and end 5 to get the whole word. 
                                                                #That's why it's crucial to add end with one on the last character of the word.
                    words.append(line[start:end])                  #Add the word to words.
                    start = end
                elif line[end].isdigit():
                    while end < len(line) and line[end].isdigit():
                        end += 1
                    words.append(line[start:end])
                    start = end
                else:
                    end += 1
                    words.append(line[start])
                    start = end
    return words #words is a list with all of the different tokens as elements.

#tally all the tokens and count their appearences in the list
def countWords(words, StopWords):
    frequencies = {}
    for _ in words:
        #If a given token is NOT in stopwords, check if already in the dictionary, if so, add 1 to count(value), else we add it to the dictionary and set count to 1.
        if _ not in StopWords:
            if frequencies.get(_) == None:
                frequencies.setdefault(_,1)
            else:
                frequencies[_] = frequencies[_] + 1
    return frequencies

#sort the dictionary by count value(descending) and stores it into a list of tuples to be printed, n to set how many 
def printTopMost(frequencies, n):  
    sorted_frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))#sourced from lecture. Sorts the dictionary in descending order.
    list_of_tuples = list(sorted_frequencies.items())[:n] #Transforms the sorted dictionary to a list of tuples and shows only the first "n" amount.
    for words, numbers in list_of_tuples:
        print(f"{words}".ljust(20) + f"{numbers}".rjust(5))


