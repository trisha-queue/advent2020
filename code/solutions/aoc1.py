# manually loaded input into ipython
input = """<copypaste>"""
years = [int(year) for year in input.split('\n')]
years = sorted(years)

### part one
start = 0
while start < len(years):                   
    second = start + 1            
    while second < len(years):
        total = years[start] + years[second]
        if total < 2020:
            second += 1
        elif total == 2020:
            print("got it!")
            print(years[start] * years[second] * years[third])
            raise Exception("the end!!")
        else:
            break
    start += 1

### part two
start = 0
while start < len(years):                   
     second = start + 1            
     while second < len(years):
         third = second + 1                  
         while third < len(years):                                  
             total = years[start] + years[second] + years[third]
             if total < 2020:
                 third += 1
             elif total == 2020:
                 print("got it!")
                 print(years[start] * years[second] * years[third])
                 raise Exception("the end!!")
             else:
                 break
         second += 1
     start += 1