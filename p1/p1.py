#/usr/bin/python3

file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
cur_elf = 1
cur_cal = 0
max_elf = 0
max_cal = 0
# Strips the newline character
for line in Lines:
    count += 1
    line_clean=line.strip()
    #print("Line{}: {}".format(count, line_clean))
    if (line_clean == "" and cur_cal!=0):
        if(cur_cal>max_cal):
            print(f"elf {cur_elf} {cur_cal}")
            max_cal=cur_cal
            max_elf=cur_elf
        cur_cal=0
        cur_elf+=1
    else:
        cur_cal+=int(line_clean)
#    if count == 20:
#        break
if cur_cal!=0:
    if(cur_cal>max_cal):
        print(f"elf {cur_elf} {cur_cal}")
        max_cal=cur_cal
        max_elf=cur_elf
    cur_cal=0
    cur_elf+=1

print(f"max elf {max_elf} max_cal={max_cal}")

