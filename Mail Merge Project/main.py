with open("./Mail Merge Project/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("./Mail Merge Project/Input/Names/invited_names.txt") as n:
    names = n.readlines()
    
for name in names:
    name = name.strip()
    new_letter = letter.replace("[name]",name)
    with open(f"./Mail Merge Project/Output/ReadyToSend/letter_for_{name}.txt", "w") as to_send:
        to_send.write(new_letter)