"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    new_line = []
    
    for item in line:
        if item != 0:
            new_line.append(item)
    
    
    doubled_line = []
    
    
    for index in range(len(new_line)):
        
        if index < len(new_line)-1:
            if new_line[index] == new_line[index + 1]:
                
                doubled_line.append(new_line[index]*2)

                new_line[index + 1] = "X"
            elif new_line[index] != "X":
                doubled_line.append(new_line[index])
        else:
            if new_line[index] != "X":
                doubled_line.append(new_line[index])

   
    add_zeros = (len(line) - len(doubled_line)) * [0]
    
    
    doubled_line += add_zeros
    
    return doubled_line
    
            
print merge([4, 4, 8])

