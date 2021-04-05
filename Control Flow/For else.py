successful = False
count = 0
for number in range(3):
    count += 1
    print(f'{count} Attempt')
    if successful:
        print("successful")
        
        break
else:
    print("Attempted 3 times and failed")
