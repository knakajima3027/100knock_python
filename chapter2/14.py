N = input()
count = 0
with open('hightemp.txt') as input_file:
      for line in input_file:
          print(line)
          count += 1
          if count == int(N):
              break
