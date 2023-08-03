# 1
# def msum(*args):
#   S = 0
#   for i in args:
#     if type(i) != int:
#       print("Must be integer")
#       return None
#     S+=i
#   return S
# print(msum(8,9,10))

# 2
# def strsum(*args):
#   cnt = 0
#   for i in args:
#     if type(i) == str:
#       cnt+=1
#   return cnt
# print(strsum("the",6,6.5,"you"))

# 3
# def average(*args):
#   S = 0
#   for i in args:
#     if type(i) == int or type(i) == float:
#       S+=i
#   if S != 0:
#     P=S/len(args)
#     return P
#   return None
# print(average(7,9,5))

# 4
# def math(a,b):
#   if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
#     return a+b,a-b,a*b,a/b
#   return None
# print(math(8,7))

# 5
# def up(mstr):
#   if type(mstr) != str:
#     print("Should be string")
#     return None
#   tmp = ""
#   for i in mstr:
#     if ord(i)>=97 and ord(i)<=122:
#       tmp+=chr(ord(i)-32)
#     else:
#       tmp+=i
#   return tmp
# print(up("hello"))

# 6
def low(mstr):
  if type(mstr) != str:
    print("Should be string")
    return None
  tmp = ""
  for i in mstr:
    if ord(i)>=65 and ord(i)<=90:
      tmp+=chr(ord(i)+32)
    else:
      tmp+=i
  return tmp
print(low("HELLO"))
