import time



with open('data.txt') as f:
    spending = [int(line.rstrip()) for line in f]


if __name__ == "__main__":
  replit_start_time = time.perf_counter()


target_number = 2020

for i, number in enumerate(spending[:-1]): 
    complementary = target_number - number
    if complementary in spending[i+1:]:  
      print(number)
      print(complementary)
      ans = number * complementary
      print(ans)
   
for line in spending:
  for line2 in spending:
    for line3 in spending:
      if line + line2 + line3 == 2020:
        print(line * line2 * line3)




 
  
replit_end_time = time.perf_counter()
print("Elapsed time:", replit_end_time - replit_start_time)