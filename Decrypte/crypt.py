import string
def crypt(message,pas):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    result=""
    for i in message:
        position=caracteres.find(i)
        if position<len(caracteres)-pas:
            result+=caracteres[position+pas]
        else:
            result+=caracteres[0+pas-(len(caracteres)-position)]
    return(result+str(pas))