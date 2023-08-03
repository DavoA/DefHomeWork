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
# def low(mstr):
#   if type(mstr) != str:
#     print("Should be string")
#     return None
#   tmp = ""
#   for i in mstr:
#     if ord(i)>=65 and ord(i)<=90:
#       tmp+=chr(ord(i)+32)
#     else:
#       tmp+=i
#   return tmp
# print(low("HELLO"))

# 7
# def mytitle(mstr):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   nmstr = ""
#   for i in range(len(mstr)):
#     if mstr[i] == mstr[0] or mstr[i-1] == " ":
#       nmstr+=mstr[i].upper()
#     else:
#       nmstr+=mstr[i]
#   return nmstr
# sentence = "hello  world"
# print(mytitle(sentence))

# 8
# def myreverse(mstr):
  # if type(mstr) != str:
  #   print("Should be string")
  #   return None
#   tmp=""
#   for i in range(len(mstr)-1,-1,-1):
#     tmp+=mstr[i]
#   return tmp
# print(myreverse("hello"))

# 9
# def substr(mstr,a,b):
#   if type(mstr) != str or type(a) != int or type(b) != int:
#     print("Wrong")
#     return None
#   index1 = 0
#   index2 = 0
#   for i in range(len(mstr)):
#     if mstr[i] == str(a):
#       index1 = i
#   for i in range(len(mstr)):
#     if mstr[i] == str(b):
#       index2 = i
#   if index2!=0:
#     return mstr[index1+1:index2]
# print(substr("hello6 my good 7world",6,7))

# 10
# def longword(mstr):
#   if type(mstr) != str:
#     print("Should be string")
#     return None
#   arr=mstr.split()
#   l = 0
#   word = ""
#   for i in arr:
#     if len(i)>l:
#       l=len(i)
#       word = i
#   return word
# print(longword("Hello my wonderful world"))

# 11
# def mostused(mstr):
#   if type(mstr) != str:
#     print("Should be string")
#     return None
#   max = 0
#   letter = ""
#   for i in mstr:
#     if mstr.count(i)>max:
#       max=mstr.count(i)
#       letter = i
#   return letter
# print(mostused("Hello World"))

# 12
def longword_mostused(mstr):
  if type(mstr) != str:
    print("Should be string")
    return None
  arr=mstr.split()
  l = 0
  word = ""
  for i in arr:
    if len(i)>l:
      l=len(i)
      word = i
  max = 0
  letter = ""
  for i in word:
    if mstr.count(i)>max:
      max=mstr.count(i)
      letter = i
  return letter
print(longword_mostused("Hello my colorful world"))
