name = "Siddhant Prateek"
print(len(name))
print(name.upper())
print(name.lower())
print(name.replace('d', ' '))
print(name.replace(' ', '0'))
print('S' in name)  # THIS CODE GENERALLY VERIFY THE PRESENCE OF SYNTAX
print('s' in name)  # THIS CODE GENERALLY VERIFY THE PRESENCE OF SYNTAX

print(name.find('Siddhant'))  # SINCE THE NAME SIDDHANT STARTS FROM INDEX 0
print(name.find('Prateek'))
print(name[0:5])  # print all character from 0 to 4
print(name[-2])
#  'Siddhant Prateek'
#   01234567........
# IF YOU DON'T INCLUDE 1ST INDEX IN PYTHON BY DEFAULT TAKE FROM '0'
print(name[:5])
# IF YOU DON'T INCLUDE LAST INDEX IN PYTHON BY DEFAULT PRINT TILL THE END
print(name[0:])
# IF YOU DON'T INCLUDE INDEX IN PYTHON IT WILL THE COPY OF THE STRING
print(name[:])
