import csv

myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B'],
          ['Mia', 'Smith', 'A'],
          ['Max', 'Blur', 'C']]
 
myFile = open('file.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("csv generating complete. \nFilename -> file.csv \nThe delimeter is ','")
