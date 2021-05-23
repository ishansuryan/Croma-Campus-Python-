# Why Python?
# a = int(input("Enter a numnber"))
# b = int(input("Enter a numnber"))
# print('the sum is:', a+b)

'''
Code for above program in c++

#include<iostream.h>
#include<conio.h>
void main(){
    int a,b,c
    cout<<"Enter a number";
    cin>>a;
    cout<<"Enter a number";
    cin>>b;
    c = a+b
    cout<<"The sum is"<<c;
}
'''
# import random
# otp = random.randint(1000,9999)
# print('opt is:',otp)
# def smart_devide(func):
#     def inner(a,b):
#         if b == 0 :
#             print("Devision by zero is not defined")
#             return
        
#         return func(a,b)
#     return inner

# # @smart_devide
# def devide(a,b):
#     return a/b
# devide = smart_devide(devide)

# print(devide(10,0))

# from test import devide
# from test import devide
# print(devide(10,0))   

def add(**kwargs):#,**kwargs):
    # print('type of a is' ,type(a))
  
    # s = 0
    # for i in a:
    #     s += i
    if kwargs:
        print('type of kwargs is' ,type(kwargs))
        print(kwargs)
    # return s
    

# print(add(1,2,3,4,5,6))
# print(add(1,2,3))
print(add(v = 'C',d = 20,l = []))

