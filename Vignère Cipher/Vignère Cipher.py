def encrypt_text(text, keyword):
    text = text.lower()
    keyword = keyword.lower()
    
    counter_text = 0
    counter_keyword = 0
    
    text_list = list(text)
    keyword_list = list(keyword)
    encrypt_list = []
    for element in text_list:
        if counter_text >= len(keyword):
            counter_text = 0
        new_element = keyword_list[counter_text]
        shift = calculate_shifts(new_element)
        letter = encrypt_letter(element, shift)
        encrypt_list.append(letter)
       # encrypt_list..append(new_element)
        counter_text += 1
    
    encrypted_text = "".join(encrypt_list)
    
    #shifts_list = []
   # for element in encrypt_list:
    #    shift = calculate_shifts(element)
    
#        shifts_list.append(shift)
    return encrypted_text


def calculate_shifts(letter):
    alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    position = alphabet_list.index(letter)

    return position


def encrypt_letter(caracter, key):
    alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alpha = caracter.isalpha()
    if alpha == True:
        encrypted_index = alphabet_list.index(caracter) + key
        if encrypted_index >= 25:
            encrypted_caracter = alphabet_list[encrypted_index - 26]
        else:
            encrypted_caracter = alphabet_list[encrypted_index]
        
        return encrypted_caracter
    else:
        return caracter


text = input("Which text should be encrypted: ")
keyword = input("Which keyword should be used?")
print(encrypt_text(text,keyword))
    
    