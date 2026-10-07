
name = input("What is your name? ")
print(f"Hello {name}")
last_name= input("What is your last name? ")
mark = int(input("What did you get? "))
if mark <= 50: 
    print(f"Pathetic! {last_name}")
elif mark <= 80:
    print(f"it's ok lah.. {name}")    
else:
    print(f"wow! {name} you sure deserve a pudding")    

