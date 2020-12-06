# manually loaded the input into a variable called "map"
input = """<copy_paste"""
map = input.split('\n')

### part one (copied into ipython)
curr_y = curr_x = count = 0
while curr_y < len(map):
    if map[curr_y][curr_x] == '#':                                                             
        count += 1
    curr_x = (curr_x + 3) % len(map[curr_y])
    curr_y += 1  
print(count)


### part two
def calc(right, down):  
     curr_x = curr_y = count = 0                                                                
     while curr_y < len(map):    
         if map[curr_y][curr_x] == '#':
             count += 1                                       
         curr_x = (curr_x + right) % len(map[curr_y])
         curr_y += down 
     print(count) 

# just ran the above in ipython manually changing the inputs, and then multiplied the results in ipython