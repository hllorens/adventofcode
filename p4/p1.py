#/usr/bin/python3



file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
elements=[]
full_overlap=0
# Strips the newline character
for line in Lines:
    count += 1
    line_clean=line.strip()
    #print("Line{}: {}".format(count, line_clean))
    if (line_clean == ""):
        continue
    else:
        line_arr=line_clean.split(",")
        range1=line_arr[0].split("-")
        range2=line_arr[1].split("-")
        if (int(range1[0])>=int(range2[0]) and int(range1[1])<=int(range2[1])) or (int(range2[0])>=int(range1[0]) and int(range2[1])<=int(range1[1])):
            full_overlap+=1
            print(f"{line_clean} full_overlap={full_overlap}")
    if count == -1:
        break


print(f"Total {full_overlap}")
