from ast import Or
from turtle import color
import matplotlib.pyplot as plt

invoice = open('CupcakeInvoices.csv')

for line in invoice:
    print(line)

invoice.seek(0, 0)

for cupcake in invoice:
    type = cupcake.split(",")
    for flavor in type:
        if flavor.startswith("Choc") or flavor.startswith("Vani") or flavor.startswith("Straw"):
            print(flavor)

invoice.seek(0, 0)

total = 0

for order in invoice:
    split = order.rstrip("\r\n").split(",")
    total += float(split[3]) * float(split[4])
    print(float(split[3]) * float(split[4]))

print(total)

invoice.seek(0, 0)

flavors = ["Chocolate", "Vanilla", "Strawberry"]
values = [0, 0, 0]

for order in invoice:
    split = order.rstrip("\r\n").split(",")
    if split[2] == "Chocolate":
        values[0] += int(round(int(split[3]) * float(split[4])))
    elif split[2] == "Vanilla":
        values[1] += int(round(int(split[3]) * float(split[4])))
    elif split[2] == "Strawberry":
        values[2] += int(round(int(split[3]) * float(split[4])))


print(values)

Colors = ["brown", "teal", "purple"]


plt.bar(flavors, values, color=Colors)
plt.title("Ice cream sales", fontsize=20)
plt.xlabel("Ice Cream Flavors", fontsize=14)
plt.ylabel("Total Sales", fontsize=14)
plt.show()

invoice.close()



