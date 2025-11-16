string = ""
bar = int(input("masukkkan angka : "))
while bar >= 0:
  kol = bar
  
  while kol > 0:
      string = string + " * "
      kol = kol - 1
  string = string + "\n"
  bar = bar - 1
    
print(string)