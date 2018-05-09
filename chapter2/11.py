input_file = open('hightemp.txt', 'r')
output_text = open('result.txt', 'a')
for line in input_file:
    output_line = line.replace('\t', ' ')
    output_text.write(output_line)
    print(output_line)
