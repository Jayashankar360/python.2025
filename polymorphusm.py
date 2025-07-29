class Bank():
    def getroi(self):
        return 10;
class Sbi(Bank):
    def getroi(self):
        return 7;
class Icici(Bank):
    def getroi(self):
        return 8;
b1=Bank() #it face method overridng so we can create every class have supparte object
b2=Sbi()
b3=Icici()
print("bank of rate interst:",b1.getroi())
print("bank of rate interst:",b2.getroi())
print("bank of rate interst:",b3.getroi())
