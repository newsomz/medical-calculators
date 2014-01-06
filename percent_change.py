def percent_change(size1, size2):
   """(num, num) -> float

   Return the percent change from size1 to size2 and print the 
   percent change. If no change print 'No change in size.'

   >>> percent_change(2184, 1623)
   26% smaller
   >>> percent_change(850, 2077)
   144% larger
   >>> percent_change(445, 445)
   No change in size
   """
   change = ((size2 * 100) // size1) - 100


   if change < 0:
       return str(round(abs(change))) + "% smaller"
   elif change > 0:
       return str(round(change)) + "% larger"
   elif change == 0:
       return "No change in size"

#Have user enter initial spleen/liver measurement
size1 = float(input('Enter initial measurement: '))

#Have user enter second spleen/liver measurement 
size2 = float(input('Enter second measurement: '))

#Print the percent change between intial & second measurement
print(percent_change(size1, size2))
