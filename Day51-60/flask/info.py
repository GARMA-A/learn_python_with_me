# Decorator 
def DecoratorFunction(func):
       
       def wraperFunction(*args):
              print("Before")
              func(*args)
              print("After")
       return wraperFunction




def say_hello():
       print("Hello")

       
# ------------------------
# Old Way 
# afterDecoration = DecoratorFunction(say_hello)
# afterDecoration("repo" , "bebo")
# ------------------------
# New Way 
@DecoratorFunction
def say_hello(*args):
       print(f"Hello:{args[0]},{args[1]}")

say_hello("repo" , "bebo")
# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------



# def decrator(func , a="nothing" , b="nothing"):
#        def wraper():
#               print(f"extra a = {a} , extra b = {b}")
#               func(a,b)
#        return wraper



# def say_hello(name1 = "GARMA" , name2 = "girgis"):
#        print("------------------------")
#        print("Hello")
#        print(name1 +" "+ name2)
#        print("Welcome to decoratores")
#        print("------------------------")
       
# # Old way
# # wr = decrator(say_hello )
# # wr( "girgis" , "emad")
# # new way
# @decrator
# @DecoratorFunction 
# def say_hello(name1 = "GARMA" , name2 = "girgis"): 
#        print("------------------------")
#        print("Hello")
#        print(name1 +" "+ name2)
#        print("Welcome to decoratores")
#        print("------------------------")


# say_hello()
# # -----------------------------------------------------



# # import time
# # def speed_calc_decorator(function):
    
# #     def wrapper():
# #      now = time.time()
# #      function()
# #      print(f"The function is taking {round(time.time()-now,3)}ms " , end="")
# #      print("to finish runing" )
# #     return wrapper
    
    
# # @speed_calc_decorator
# # def slow_Calculations():
# #      for i  in  range(10000000):
# #          i * i 
    
# # slow_Calculations()
# # # -------------------------------------------
# # # -------------------------------------------
# # # -------------------------------------------
# # # -------------------------------------------

# # def DecoratorFunction(arg1="default1", arg2="default2"):
# #     def decorator(func):
# #         def wrapper(*args, **kwargs):
# #             print(f"Decorator with arguments: {arg1}, {arg2}")
# #             func(*args, **kwargs)
# #             print("After")
# #         return wrapper
# #     return decorator

# # def decrator(extra_a="nothing", extra_b="nothing"):
# #     def decorator(func):
# #         def wrapper(*args, **kwargs):
# #             print(f"Extra a = {extra_a}, Extra b = {extra_b}")
# #             func(*args, **kwargs)
# #         return wrapper
# #     return decorator

# # @DecoratorFunction(arg1="value1", arg2="value2")
# # @decrator(extra_a="valueA", extra_b="valueB")
# # def say_hello(name1="GARMA", name2="girgis"):
# #     print("------------------------")
# #     print("Hello")
# #     print(name1 + " " + name2)
# #     print("Welcome to decorators")
# #     print("------------------------")




