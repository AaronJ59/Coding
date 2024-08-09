class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity is a negative")
        else:
            self.cookiejarcapacity = capacity
            self.cookiejar_with_deposit = 0


    def __str__(self):
        result = ""
        for cookies in range(self.cookiejar_with_deposit):
            result += "🍪"
        return result



    def deposit(self, n):
        self.cookiejar_with_deposit = self.cookiejar_with_deposit + n

        if self.cookiejar_with_deposit > self.cookiejarcapacity:
            raise ValueError("You are adding more cookies than the capacity")

    def withdraw(self, n):
        self.withdrawcookies = n
        if self.withdrawcookies > self.cookiejar_with_deposit:
            raise ValueError("you are removing more cookies than there are cookies")
        else:
            self.cookiejar_with_deposit = self.cookiejar_with_deposit - self.withdrawcookies


    @property
    def capacity(self):
        return self.cookiejarcapacity

    @property
    def size(self):
        return self.cookiejar_with_deposit



# Usage
jar = Jar()  # Create an instance of Jar
jar.deposit(2)  # Deposit 2 cookies
jar.deposit(5)  # Deposit 5 more cookies

print(f"The jar currently has {jar.size} cookies.")  # Should print "The jar currently has 7 cookies."
print(jar)  # Should print 7 cookie emojis
