
def fileOperation(infile):
  try:
   with open(infile,'r') as input:
     for line in input:
       print(line)

  except:
    print("File Not found")

def workingWithStrings(mikustr):
  temp = ""
  for i in range(len(mikustr)):
    # print(mikustr[i])
    temp = mikustr[i] + temp
  temp = temp.strip()
  print(temp)
  
  if temp == mikustr:
    print("is Pallindrome")
  else:
    print("not Pallindrome")


if __name__ == "__main__":

 str = input("Enter some string yo: ")
 workingWithStrings(str.lower())

# inp = input("Enter Source File Name Bruh: ")
# fileOperation(inp)


