### This Python script reads a .txt file, count things in the file, and output a new txt file

# Read the txt file
fhand = open('romeo-full.txt')

# Define variables to count things
countLines = 0 # count lines
countRomeo = 0
countJuliet = 0
# more variables to count other things

# Loop through each line to count things
for line in fhand:
    countLines = countLines + 1
    # more code to count things
    if line.startswith("ROMEO"):
        countRomeo = countRomeo + 1
    elif line.startswith("JULIET"):
        countJuliet = countJuliet + 1

# Create an output.txt file
fout = open('output.txt', 'w')
fout.write(f"Lines of text: {countLines}\n")
fout.write(f"Romeo: {countRomeo}\n")
fout.write(f"Juliet: {countJuliet}\n")

# Close the file
fhand.close()
fout.close()

print(f"Lines of text: {countLines}")
print(f"Romeo: {countRomeo}")
print(f"Juliet: {countJuliet}")