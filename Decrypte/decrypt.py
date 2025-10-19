import string
def decrypt(message,pas):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    message=message[:len(message)-1]
    result=""
    for i in message:
        position=caracteres.find(i)
        if position!=0:
            result+=caracteres[position-pas]
        else:
            result+=caracteres[0-pas]
    return(result)