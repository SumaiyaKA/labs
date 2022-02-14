# Author: Sumaiya Al Amri - D17126680
# Date: 11.11.2021
import operator
import collections
import sys

def freq():
    text = input("Enter your text: ").upper()
    to_plain = input("Would you like to see the possible plaintext by frequency? Y or y for Yes. N or n for No\n").upper()
    
    text = text.replace(" ", "")
    text_len = len(text)
    count_freq = {char : text.count(char) for char in set(text)} 
    freq_table = {}
    for i in count_freq:
        freq_table[i] = count_freq[i] * 100 / text_len
        
    #  sort by value reverse (more frequent til less)
    sorted_freq = sorted(freq_table.items(), key=operator.itemgetter(1), reverse=True)
    sorted_freq = collections.OrderedDict(sorted_freq)
    for i in sorted_freq:
        print( i,": ", "{:.2f}".format(sorted_freq[i]) )
    
    # to decode the encrypted letters 
    if to_plain == "Y":
        # give the user range of letters 
        # to prevent exceeding the index length of the encrypted letters
        print("Range of possible plaintexts letters (between 1 - ", str(len(sorted_freq))," )\n")
        limit = int(input("Enter number of top letters to be decoded: "))
        #  check if input limit is valid
        if limit > 26 or limit > len(sorted_freq):
            print("Error: Invalid Limit!")
            sys.exit()
        decode(sorted_freq, limit)
    
def decode(sorted_freq, limit):
    letter_Freq = {'E' : 12.0,
    'T' : 9.10,
    'A' : 8.12,
    'O' : 7.68,
    'I' : 7.31,
    'N' : 6.95,
    'S' : 6.28,
    'R' : 6.02,
    'H' : 5.92,
    'D' : 4.32,
    'L' : 3.98,
    'U' : 2.88,
    'C' : 2.71,
    'M' : 2.61,
    'F' : 2.30,
    'Y' : 2.11,
    'W' : 2.09,
    'G' : 2.03,
    'P' : 1.82,
    'B' : 1.49,
    'V' : 1.11,
    'K' : 0.69,
    'X' : 0.17,
    'Q' : 0.11,
    'J' : 0.10,
    'Z' : 0.07 }

    # get it into one string 
    encrypted_freq = ""
    for key in sorted_freq.keys():
        encrypted_freq += key
    # print(string_freq)
    english_freq = ""
    for key in letter_Freq.keys():
        english_freq += key

    for i in range(limit):
        print(encrypted_freq[i], "is more likely to be --> ", english_freq[i])




def main():
    freq()



if __name__  == '__main__':
    main()