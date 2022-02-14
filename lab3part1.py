# Author: Sumaiya Al Amri - D17126680
# Date: 11.11.2021
import sys
import numpy as np

def hill_encryption():
    msg = input("Enter your message:").upper()
    msg = msg.replace(" ", "")

    # check if the message length is odd
    # if so make it even by adding an extra char at the end:
    check_len = 0
    if len(msg) % 2 != 0:
        msg += "0"
        check_len = 1
    
    # set msg to a matrix
    row = 2
    col = int(len(msg)/2)
    msg2mat = np.zeros((row, col), dtype=int)

    itr_1 = 0 
    itr_2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2mat[0][itr_1] = int(ord(msg[i]) - 65)
            itr_1 += 1
        else:
            msg2mat[0][itr_2] = int(ord(msg[i]) - 65)
            itr_2 += 1
    
    #  2 * 2 key 
    key  = input("Enter key (4 letters only):").upper()
    key = key.replace(" ", "")
    itr_3 = 0
    key2mat = np.zeros((2,2), dtype=int)
    # print("inside the for loop")
    for i in range(2):
        for j in range(2):
            key2mat[i][j] = ord(key[itr_3]) - 65 
            itr_3 += 1
            # print("key2mat[%d][%d]= %s", i, j, key2mat[i][j])

    #  get the key determinate 
    key_deter = (key2mat[0][0] * key2mat[1][1]) - (key2mat[0][1] * key2mat[1][0])
    key_deter = key_deter % 26
    # print("key_deter", key_deter)

    #  check the validation of the key
    key_mult_inv = -1 
    for i in range(26):
        temp = key_deter * i
        if temp % 26 == 1:
            key_mult_inv = i
            break
        else:
            continue

    if key_mult_inv == -1:
        print("Error: Invalid Key!\n")
        sys.exit()
    
    c_text = ""
    itr_count = int(len(msg)/2)
    if check_len == 0:
        for i in range(itr_count):
            temp1 = (msg2mat[0][i] * key2mat[0][0]) + (msg2mat[1][i] * key2mat[0][1])
            c_text += chr((temp1 % 26) + 65)
            temp2 = (msg2mat[0][i] * key2mat[1][0]) + (msg2mat[1][i] * key2mat[1][1])
            c_text += chr((temp2 % 26) + 65)
    else:
        for i in range(itr_count-1):
            temp1 = (msg2mat[0][i] * key2mat[0][0]) + (msg2mat[1][i] * key2mat[0][1])
            c_text += chr((temp1 % 26) + 65)
            temp2 = (msg2mat[0][i] * key2mat[1][0]) + (msg2mat[1][i] * key2mat[1][1])
            c_text += chr((temp2 % 26) + 65)
    
    print("Encryption text: \n%s\n", c_text)


def main():
    print("Menu:-\n1.Encryption.\n2.Decryption.\n")
    select = int(input("Enter your selection:"))
    if select == 1:
        print("Encryption:\n")
        hill_encryption()
    else:
        print("Error: Invalid Selection!\n")


if __name__  == '__main__':
    main()