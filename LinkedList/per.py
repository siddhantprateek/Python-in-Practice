def permute(unproc, proc= ""):



    
i = len(unproc)
while i > 0:
    for index in range(len(unproc) - i): 
        result.append(unproc[index: index + i])
        
