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
# def longword_mostused(mstr):
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
#   max = 0
#   letter = ""
#   for i in word:
#     if mstr.count(i)>max:
#       max=mstr.count(i)
#       letter = i
#   return letter
# print(longword_mostused("Hello my colorful world"))

# 13
# def numindex(mstr,num):
#   if type(mstr) != str or type(num) != int:
#     print("Should be string")
#     return None
#   return mstr[num],mstr[-num]
# print(numindex("Hello",1))

# 14
# def polindrom(num):
#   if type(num) != int:
#     print("Should be integer")
#     return None
#   tmp = str(num)
#   half = len(tmp1)//2
#   if tmp1 == tmp1[::-1]
#     return True
#   return False
# print(polindrom(121))

# 15
# def nearpol(num):
#   low = num-1
#   high = num+1
#   while str(low) != str(low)[::-1]:
#     low-=1
#   while str(high) != str(high)[::-1]:
#     high+=1
#   if num - low < high - num:
#     return low
#   else:
#     return high
# print(nearpol(144))

# 16
# def multiplenum(num):
#   if type(num) != int:
#     print("Should be integer")
#     return None
#   if num<10:
#     return num
#   tmp = str(num)
#   num1 = int(tmp[0])
#   num2 = int(tmp[len(tmp)-1])
#   return num1*num2
# print(multiplenum(244))

# 17
# def cntstr(ml):
#   if type(ml) != list:
#     print("Should be list")
#     return None
#   cnt = 0
#   for i in ml:
#     if type(i) == str:
#       cnt+=1
#   return cnt
# print(cntstr(["hello",90,9.8,"world"]))

# 18
# def mmax(ml):
#   if type(ml) != list:
#     print("Should be list")
#     return None
#   arr = []
#   for i in ml:
#     if type(i) == int:
#       arr.append(i)
#   return max(arr)
# print(mmax([90,18,"goog",False]))

# 19
# def evennum(ml):
#   if type(ml) != list:
#     print("Should be list")
#     return None
#   arr = []
#   for i in ml:
#     if type(i) == int:
#       if (i>=10 and i<=99) and i%2==0:
#         arr.append(i)
#   return arr
# print(*evennum([97,88,44,134,"sun",False]))

# 20
# def mlaverage(ml):
#   if type(ml) != list:
#     print("Should be list")
#     return None
#   arr = []
#   for i in ml:
#     if type(i) == int:
#       arr.append(i)
#   S = 0
#   for i in arr:
#     S+=i
#   P = S/len(arr)
#   return P
# print(mlaverage([78,90,18,"goog",False]))

# 21
# def lenlist(ml):
#   if type(ml) != list:
#     print("Should be list")
#     return None
#   arr = []
#   for i in ml:
#     if type(i) != str:
#       print("Should be str")
#       return None
#     arr.append(len(i))
#   return arr
# print(lenlist(["sos","hello","no"]))

# 22
# def ordered(ml):
#   if type(ml) != list:
#     print("Should be list")
#     return None
#   arr = []
#   for i in ml:
#     if type(i) == int:
#       arr.append(i)
#   return sorted(arr)
# print(ordered([90,"hello", True, 56, 11, 89]))

# 23
# def ordered_str(ml):
#   if type(ml) != list:
#     print("Should be list")
#     return None
#   arr = []
#   for i in ml:
#     if type(i) == str:
#       arr.append(i)
#   n = len(arr)
#   for i in range(n):
#     for j in range(n-1-i):
#       if len(arr[j]) > len(arr[j+1]):
#         arr[j], arr[j+1] = arr[j+1], arr[j]
#   return arr
# print(ordered_str(["cool","green","sos"]))

# 24
def aeoui(ml):
  if type(ml) != list:
    print("Should be list")
    return None
  letters = "aeoui"
  word = ""
  max = 0
  for i in ml:
    if type(i) != str:
      print("Should be str")
      return None
    cnt=0
    for j in letters:
      if j in i:
        cnt+=1
    if cnt > max:
      max=cnt
      word = i
  return word
print(aeoui(["sos","hello","no"]))
