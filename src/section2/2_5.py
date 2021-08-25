sub, grat = eval(input("Enter the subtotal and a gratuity rate: "))
gratper = grat / 100
grattot = sub * gratper
total = sub + grattot
print("The gratuity is", grattot, "and the total is", total)