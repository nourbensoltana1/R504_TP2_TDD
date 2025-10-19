import string
def crypt(message,pas):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    result=""
    for i in message:
        position=caracteres.find(i)
        if position<len(caracteres)-1:
            result+=caracteres[position+pas]
        else:
            result+='a'
    return(result+str(pas))