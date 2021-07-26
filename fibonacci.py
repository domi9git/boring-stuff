def main():
 iteration = int(input("enter iterations "))
 iteration2 = 2
 f0 = 0
 f1 = 1
 fn = 0
 if iteration == 0:
  print()
 if iteration == 1:
  print(f0)
 if iteration > 1:
  print(f0)
  print(f1)
 while iteration2 < iteration:
  fn = f0 + f1
  f0 = f1
  f1 = fn
  iteration2 += 1
  print(fn)

if __name__ == '__main__':
 main()