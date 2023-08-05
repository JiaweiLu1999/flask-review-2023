# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as letter_file:
    with open("Input/Names/invited_names.txt") as name_file:
        name_list = [name.strip() for name in name_file.readlines()]
        lines = letter_file.readlines()
        for name in name_list:
            with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as invitation_file:
                invitation_file.write(lines[0].replace("[name]", name))
                for line in lines[1:]:
                    invitation_file.write(line)




