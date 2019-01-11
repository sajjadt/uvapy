num_cases = int(input())

for i in range(num_cases):
  text = input()

  freq = {ch:0 for ch in "MARGIT"}
  for ch in text:
    if ch in freq:
      freq[ch] += 1
  
  print(
    min([freq["M"], freq["A"]//3, freq["R"]//2, freq["G"], freq["I"], freq["T"]]))
  