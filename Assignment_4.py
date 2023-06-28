#Shravan Surve 
#Demonstrate the use of loop manipulation statements.


# 1)break
for i in "Shravan":
    if i=="h":
        break
    else:
        print(i)

i=5
while i<=10:
    if i==5:
        break
    else:
        print(i)

# 2)continue
for i in "Shravan":
    if i=="h":
        continue
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        continue
    else:
        print(i)

# 3)pass
for i in "Shravan":
    if i=="q":
        pass
    else:
        print(i)

i=4
while i<=10:
    if i==5:
        pass
    else:
        print(i)

# 4)for with else loop
for i in "Shravan":
    if i=="e":
        break
    else:
        print(i)
else:
    print("This has break")

for i in "Shravan":
    if i=="k":
        pass
    else:
        print(i)
else:
    print("This has pass")


for i in "Shravan":
    if i=="h":
        continue
    else:
        print(i)
else:
    print("This has continue")

# 5)while with else loop
i=1
while i<=10:
    if i==5:
        break
    else:
        print(i)
else:
    print("This has break")

i=1
while i<=10:
    if i==5:
        continue
    else:
        print(i)
else:
    print("This has continue")

i=1
while i<=10:
    if i==5:
        pass
    else:
        print(i)
else:
    print("This has pass")

