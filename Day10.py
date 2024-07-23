def format_name(str):
       formated = ""
       if(len(str)>0):
        strWords = str.split(' ')
        for word in strWords:
            formated+=f"{word[0].upper()}{word[1:].lower()} "
       return formated or str
       
def format_name_With_Title(str):
    format =""
    if(len(str)>0):
        format = str.title()
    return format
            
words = input('Enter your full name : ')
print(format_name_With_Title(words))