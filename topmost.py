import sys
import wordfreq as wf
import urllib.request

def main(stopwordsfile, textfile, n):
    #The stopwords file is assumed to always be a textfile in your folder, not a URL, as per instruction.
    #Here we open and read then split the file, which is now a long string, into a list of words with "\n" as a separator.
    with open(stopwordsfile, encoding="utf-8") as inp_stopwords_file: 
        stop_lines = inp_stopwords_file.read().splitlines()
    #If a URL is given instead of a local directory, excecute this code
    if textfile.startswith("http://") or textfile.startswith("https://"):
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
    #else excecute this code. The splitting of the textfile works the same as the stopwords file.
    else:
        with open(textfile, encoding="utf-8") as inp_text_file:
            lines = inp_text_file.read().splitlines()
    #Any possible blank spaces left in the lines will be removed by the function tokenize
    number_of_printed_words = int(n) #n is treated as a string if nothing else is given. We need to transform it to an integer.

    wf.printTopMost(wf.countWords(wf.tokenize(lines), stop_lines), number_of_printed_words) #Implementation of the functions from the wordfreq module

if __name__ == "__main__": 
    main(sys.argv[1], sys.argv[2], sys.argv[3])
