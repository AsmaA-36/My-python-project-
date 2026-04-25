#Assignment1
print('Welcome to the number Game!.')
print('What is your name?')
myname=input('>')
print('Welcome '+myname+' ,Write a number between 1-20')
#dictionary
h = {1: 'one', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty' }
write = int(input('>'))
if write > 20:
 print('Please adhere to the rules of the game, Choose any number between 1-20')
else: 
 print(h[write])
#I have questions reagard0022549428ing dictionaries

print('Congratulations!! You have come to the end of the game. ')