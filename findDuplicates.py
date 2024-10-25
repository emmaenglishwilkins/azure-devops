curr_avd = []
fall2024 = []

to_add = []

# try:
#     with open('curr_avd.csv') as csvfile:
#         lines = csvfile.readlines()
#         header = lines[0].strip().split(",")
#         # print(header)
#         for i in range(len(header)):
#             if header[i] == "displayName":
#                 idx = i 

#         for line in lines[1:]:
#             row = line.strip().split(",")
#             curr_avd.append(row[idx])

# except IOError as e:
#     print("Error reading curr_avd.csv:", e)

try:
    with open('fall2024.csv') as csvfile:
        lines = csvfile.readlines()
        header = lines[0].strip().split(",")
        # print(header)
        for i in range(len(header)):
            if header[i] == "Children Names":
                idx = i

        for line in lines[1:]:
            row = line.strip().split(",")
            fall2024.append(row[idx])

except IOError as e:
    print("Error reading curr_avd.csv:", e)


# for student in fall2024:
#     if student in curr_avd:
#         fall2024.remove(student)

try:
    with open('exportUsers_2024-10-25.csv') as csvfile:
        lines = csvfile.readlines()
        header = lines[0].strip().split(",")
        print(header[0])
        upn_idx = 0
        display_name_idx = 1
        for i in range(len(header)):
            if header[i] == "userPrincipalName":
                print("found upn_idx", i)
                upn_idx = i
            if header[i] == "displayName":
                display_name_idx = i 
            if header[i] == "id":
                id_idx = i

    id_dict = {}  # Initialize an empty dictionary
    for line in lines[1:]:  # Assuming lines contains the data rows
        row = line.strip().split(",")  # Split each line by comma
        id_value = row[id_idx]  # Get the id value
        display_name_value = row[display_name_idx]  # Get the display name value
        upn_value = row[upn_idx]  # Get the User Principal Name value
        
        # Store the values in the dictionary with id as the key
        id_dict[id_value] = (display_name_value, upn_value)  # Use a tuple or list for values
except IOError as e:
    print("Error reading exportUsers_2024-10-15.csv", e)
        

try:
    with open('to_add.csv', 'w') as csvfile:
        for student in fall2024:
            # Check if the student's name matches any displayName in id_dict
            for id_value, (display_name, upn) in id_dict.items():
                if student.lower() in display_name.lower():  # General match (case insensitive)
                    # Print the found student details including UPN
                    print("Found student:", student, "ID:", id_value, "Display Name:", display_name, "UPN:", upn)
                    
                    # Write the id, display name, and UPN to the CSV file, separated by commas
                    csvfile.write("{},{}\n".format(id_value, display_name))
                    break  # Exit the inner loop once a match is found
except IOError as e:
    print("Error writing to to_add.csv:", e)



print(len(fall2024))
