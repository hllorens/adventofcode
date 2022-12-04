#/usr/bin/python3

file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
elves=[]
cur_cal=0
cur_elf=1
# Strips the newline character
for line in Lines:
    count += 1
    line_clean=line.strip()
    #print("Line{}: {}".format(count, line_clean))
    if (line_clean == "" and cur_cal!=0):
        elves.append([cur_elf,cur_cal])
        cur_cal=0
        cur_elf+=1
    else:
        cur_cal+=int(line_clean)
#    if count == 20:
#        break
if cur_cal!=0:
    elves.append([cur_elf,cur_cal])
    cur_cal=0
    cur_elf+=1

elves_s=sorted(elves, key=lambda x: x[1])


print(f"max elf {elves_s[len(elves)-1][0]} max_cal={elves_s[len(elves)-1][1]}")
top_3_elves=elves_s[-3:]
print(top_3_elves)
print("total top 3 is "+str(top_3_elves[0][1]+top_3_elves[1][1]+top_3_elves[2][1]))
