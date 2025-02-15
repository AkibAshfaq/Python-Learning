
# Read only
file = open('C:\WOrksPace\All\Python\File Handle\ReadWrite.txt', 'r')
content = file.read()
print(content)
file.close()

# Read line by line
print("Line by line")
file = open("File Handle\ReadWrite.txt", 'r')

for line in file:
    print(line.strip())

file.close()

# Another way
file = open("File Handle\ReadWrite.txt", "r")

line = file.readline()
while line:
    print(line.strip())
    line = file.readline()  

file.close()


# Read in binaries
file = open('C:\WOrksPace\All\Python\File Handle\ReadWrite.txt', 'rb')
content = file.read()
print(content)
file.close()

# Write in a file
file = open('C:\WOrksPace\All\Python\File Handle\ReadWrite.txt', 'w')
file.write("Hello Python Write")
file.close()

# TO VIEW
file = open('C:\WOrksPace\All\Python\File Handle\ReadWrite.txt', 'r')
content = file.read()
print(content)
file.close()

# Write in a files next Line
file = open('C:\WOrksPace\All\Python\File Handle\ReadWrite.txt', 'a')
file.write("Hello Python append")
file.close()

# TO VIEW
file = open('C:\WOrksPace\All\Python\File Handle\ReadWrite.txt', 'r')
content = file.read()
print(content)
file.close()

# txt file Creation
try:
    with open("File Handle/file.txt", "x") as f:
        f.write("Created using exclusive mode.")
except FileExistsError:
    print("Already exists.")

# CSV file Read and Write
import csv

# Open the CSV file
with open("File Handle/example.csv", newline='') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    # Read and print each row
    for row in csvreader:
        print(row)
        # Saving  in list to access
        #li = list(row)
        #print(li)

# JSON file Read and Write
import json

# Open the JSON file
with open("File Handle/sample1.json", "r") as jsonfile:
    # Load the JSON data
    data = json.load(jsonfile)
    # Print the data
    print(data)
