temp = eval(raw_input("Enter Temperature:"))
while True:
    if temp>31 and temp<35:
        print ' Sunny Day '
        break
    elif temp>35 and temp<40:
        print ' warm Day '
        break
    elif temp>40 and temp<50:
        print ' High Temperature'
        break
    else:
        print ' Invalid '
        break
