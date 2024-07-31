# try :
#        lst = [1,2,3]
#        file = open("notFound.txt")
#        print(lst[3])
# except FileNotFoundError:
#        print("this file is not found")
# except IndexError:
#        print("the max index is 2")
# else:
#        content = file.read()
# finally:
#        print("finaly")
#        raise ValueError("this error just because it is 12:30Am and i cant sleep untill finish this ")
       
# you can write a big try code and use many except to handle
# differnet errors and if there is no exception else will run 
# and if there is exception except will run
# and in the end finally will run always 
# you can immediately run error (raise) usually under if statement
# ----------------------------------------

# try :
#        x = 0
#        if(x==0):
#               raise ZeroDivisionError("you can not divide by zero")
#        print(5/x)
# except ZeroDivisionError as e:
#        print(e)