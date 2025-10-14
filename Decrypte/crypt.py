import string
def crypt(message):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    result=""
    for i in message:
        position=caracteres.find(i)
        if position!=len(caracteres)-1:
            result+=caracteres[position+1]
        else:
            result+='a'
    return(result)