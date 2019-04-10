class maths:
    def sum(firstvalue,desiredvalue):
        add=firstvalue+desiredvalue
        print(add)

    def subtraction(firstnumber,desirednumber):
        sub=firstnumber-desirednumber
        print(sub)
        
    def multiply(firstnumber,desirednumber):
        mul=firstnumber*desirednumber
        print(mul)
    def division(firstnumber,desirednumber):
        try:
            div=firstnumber/desirednumber
            print(div)
        except ZeroDivisionError as msg:
            print('invalid attempt',msg)
            
    def power(firstnumber,powervalue):
        pow=firstnumber**powervalue
        print(pow)

    def squareroot(desirednumber):
        sqrt=desirednumber**(1/2)
        print(sqrt)

    

        
