N = input()
count = 0
with open('hightemp.txt') as input_file,\
      open('new.txt', 'a') as new_file:

      for line in input_file:
          new_file.write(line)
          count += 1
          if count == int(N):
              break
