import string
def crypt(message,pas):
    if not isinstance(pas, int) or pas < 1 or pas > 9:
        raise ValueError("Le pas doit être un entier entre 1 et 9")
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    result=""
    for i in message:
        position=caracteres.find(i)
        if position<len(caracteres)-pas:
            result+=caracteres[position+pas]
        else:
            result+=caracteres[0+pas-(len(caracteres)-position)]
    return(result+str(pas))