"""4) მომხმარებელს შემოატანინეთ აჯიმანიებისა და ბუქნების რაოდენობა, ტქვენ კი შეამოწმეთ უდრის ტუ არა აჯიმანიების რაოდენობა აუცილებელს ან ბუქნების რაოდენობა აუცილებელს"""

#d eclaring variable workout target

deadlift_target = 100
pushups_target = 150


# cimplited pushups , deadlifts

complited_deadlifts = int(input("how many deadlift you made?: "))
complited_pushups = int(input("how many pushups you made?: "))


# print created variables 

print(deadlift_target <= complited_deadlifts and pushups_target <= complited_pushups)
print(deadlift_target == complited_deadlifts and pushups_target == complited_pushups)

print(deadlift_target <= complited_deadlifts or pushups_target <= complited_pushups)
print(deadlift_target == complited_deadlifts or pushups_target == complited_pushups)


# if you complite pushups you won!

i = complited_pushups
if i >= 100:
    print("you won challenge!")

