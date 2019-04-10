class university:
    def cse():
        print('this is university first branch')
    class collage:
        def branch(self):
            print('its a collage and working under the university')
    class examcen:
        def center(self):
            print('this is a exam center under university')

university.cse()
u=university().collage()# this is calling inner collage class calling 
u.branch()

un=university().examcen()#here dont confuese while calling the inner class just create one object and outer class then which inner class object we are calling only that particluar class only need to call, not to call sequence of class in outer class

un.center()
