class bank:
    def __init__(self,bname,acno,amount):
        self.bname=bname
        self.acno=acno
        self.amount=amount

    def info(self):
        try:
            print('welcome to sbi bank')
            sign=int(input('enter grn number:'))
            if sign == 78900:
                pasw=int(input('enter your passcode:'))
                if pasw == 7861:
                    print('welcom to your personal banking')
                    print('select your option:')
                    print('*'*30)
                    print('\n1.deposit\n2.withdraw\n3.check balence')
                    print('*'*30)
                    options=eval(input('choose your option:'))
                    if options == 1:
                        deposit=eval(input('enter how much you want to deposit'))
                        bal=depositk
                    if options ==2 :
                        withdraw =eval(input('enter how much want to withdraw'))
                        amount=(bal-withdraw)
                        
                        print(amount)
                    if options ==3:
                        chkbl= bal
                        print('your current balence is:',bal)
            else:
                print('please choose correct option')
        except  (ValueError,TypeError,SyntaxError,BaseException,IndentationError,EOFError) as msg:
            print('please try again some thing went wrong with your options')
        else:
            print('you can add adhar card number with atm also')

        finally:
            print('thanks for using sbi atm, have a nice day')

            
