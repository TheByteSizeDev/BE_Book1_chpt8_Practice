#Practice: Activities for Kids

''' Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. 
Each function should print that the child performed the activity.For example, Jay ran like a fool! or Chantelle slid down the slide!.

The following lists of children should be iterated, and the names sent to the appropriate functions. 

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

'''

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run(name):
    print(f"{name} ran around the yard")

def swing(name):
    print(f"{name} swung the bat")

def slide(name):
    print(f"{name} slid to home")

def hide_and_seek(name):
    print(f"{name} plays hide and seek like a nerd!")

for name in running_kids:
    run(name)

for name in swinging_kids:
    swing(name)

for name in sliding_kids:
    slide(name)

for name in hiding_kids:
    hide_and_seek(name)

#