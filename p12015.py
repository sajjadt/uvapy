num_tests = int(input())
urls = []
for test in range(num_tests):
  urls = []
  for i in range(10):
    inp = input().split()
    url, value = str(inp[0]), int(inp[1])
    urls.append((url, value))
  urls.sort(key=lambda x: x[1], reverse=True)
  print("Case #" + str(test+1)+":")
  tops = [x[0] for x in urls if x[1] == urls[0][1]]
  print("\n".join(tops))
