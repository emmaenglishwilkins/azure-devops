curr_avd = []
fall2024 = []

to_add = []

try:
    with open('curr_avd.csv') as csvfile:
        lines = csvfile.readlines()
        header = lines[0].strip().split(",")
        print(header)
        for i in range(len(header)):
            if header[i] == "displayName":
                idx = i 

        for line in lines[1:]:
            row = line.strip().split(",")
            curr_avd.append(row[idx])

except IOError as e:
    print("Error reading curr_avd.csv:", e)

try:
    with open('fall2024.csv') as csvfile:
        lines = csvfile.readlines()
        header = lines[0].strip().split(",")
        print(header)
        for i in range(len(header)):
            if header[i] == "Children Names":
                idx = i

        for line in lines[1:]:
            row = line.strip().split(",")
            fall2024.append(row[idx])

except IOError as e:
    print("Error reading curr_avd.csv:", e)


for student in fall2024:
    if student in curr_avd:
        fall2024.remove(student)



try:
    with open('to_add.csv', 'w') as csvfile:
        for i in range (len(fall2024)):
            csvfile.write(fall2024[i] + '\n')
except IOError as e:
    print("Error writing to to_add.csv", e)

print(len(fall2024))
