def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08 #bill = bill * 1.08
    print("With tax: %f" % bill)
    return bill


def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15 #1.15  #!!!!bill varijabla-objekat se ne nasledjuje kroz funkcije - one su privatne unutar funkcija
    print("With tip: %f" % bill)
    return bill
#http://www.saltycrane.com/blog/2008/01/python-variable-scope-notes/
#globalne i lokalne variable unutar funkcija


meal_cost = 100
meal_with_tax = tax( meal_cost )
meal_with_tip = tip( meal_with_tax )


def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print("%d squared is %d." % (n, squared))
    return squared


# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square( 10 )