import random

def primary():
  #taking data from user and writing in the text file
  f= open("quotes.txt","a")
  input1 = input("Type some quote or text")
  f.write(input1 + "\n")
  f.close()

  #print("Keep it logically awesome.") 
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=len(quotes)-1
  print(quotes[last])
  
  #rnd=random.randint(0,last)
  #print(quotes[rnd].rstrip("\n"))
  #rnd=random.randint(0,last)
  #print(quotes[rnd].rstrip("\n"))

if __name__== "__main__":
  primary()
