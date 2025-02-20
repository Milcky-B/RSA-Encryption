from alpha import alphabet,alphabet_dec

def cipher(words:str):
    words=words.lower()
    new_word=[]
    for letter in words:
        if letter==" ":
            new_word+=" "
        else:    
            new_word.append(alphabet[letter])
    return new_word

def decipher(words):
    dec_word=""

    for letter in words:
        if letter==" ":
            dec_word+=" "
        else:   
            letter=int(letter) 
            dec_word+=alphabet_dec[letter]

    return dec_word