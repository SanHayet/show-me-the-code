import string, random

file = string.ascii_letters + string.digits

def getRadom():
    return "".join(random.sample(file,4))

def connect(group):
    return "-".join([getRadom() for i in range(group)])

#n组m个group构成
def generate(n, m):
    return [connect(m) for i in range(n)]

print(generate(5, 4))



