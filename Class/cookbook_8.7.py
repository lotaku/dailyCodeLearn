class A:
    def spam(self):
        print('A.spam')
class B(A):
    def spam(self):
        super().spam()
        print('B.spam')
# Call parent spam()
b = B()
print B.__mro__

