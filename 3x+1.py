def main():
 num = int(input("Enter a number: "))
 while num != 1:
  if (num % 2) == 0:
   num /= 2
   print(num)
  else:
   num = (num * 3) + 1
   print(num)
  
if __name__ == '__main__':
 main()