import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:8000')

n = int(input("Enter any number: "))

result = proxy.compute_factorial(n)

print("Factorial:",result)

