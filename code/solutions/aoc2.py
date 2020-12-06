import re

# manually loaded the input into a variable called "map"
input = """<copy_paste"""
passwords = input.split('\n')

### part one
total = 0
for entry in passwords:
     min_letter, max_letter, letter, entry = re.match("(\d+)-(\d+) (\w): (\w+)", entry).groups()
     min_letter = int(min_letter)
     max_letter = int(max_letter)
     count = 0
     for x in entry:                  
         if x == letter:
             count += 1               
     if min_letter <= count and count <= max_letter:
         total += 1
print(total)

### part two
total = 0
for entry in passwords:                                      
     min_letter, max_letter, letter, entry = re.match("(\d+)-(\d+) (\w): (\w+)", entry).groups()
     min_letter = int(min_letter)
     max_letter = int(max_letter)                    
     count = 0                                                
     if entry[min_letter-1] == letter:               
         count += 1     
     if entry[max_letter-1] == letter:            
         count += 1                                 
     if count == 1:                        
         total += 1
print(total)