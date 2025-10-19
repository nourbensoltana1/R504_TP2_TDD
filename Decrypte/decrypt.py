import string
def decrypt(message):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    result=""
    for i in message:
        position=caracteres.find(i)
        if position!=0:
            result+=caracteres[position-1]
        else:
            result+=' '
    return(result)