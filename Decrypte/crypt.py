import string
def crypt(message):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    result=""
    for i in message:
        position=caracteres.find(i)
        result+=caracteres[position+1]
    return(result)