
def check(a):

 length=len(a)

 if length==0 or length==1:

   return True

 return a[0]<a[1] and check(a[1:])

a=[56,23,54,69,89,76,21,3,58]

b=[23,36,45,65,89,98]

if check(a):

print('Given list is sorted')

else:

 print('Given list is not sorted')

if check(b):

 print('Given list is sorted')

else:

 print('Given list is not sorted')