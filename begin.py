# or we can do it in one line, siomply by using the strip() and title() methods together.
name = input('what is ur name ? ').strip().title()

# remove whitespave from str 
#name = name.strip() 

#capitalize user's name 
#name = name.capitalize()

#capitalize all the very first letter 
#name = name.title()

# or we can do it in one line
#name = name.strip().title()

#slit user name into first and last name
first, last = name.split(" ")

print(f"hello, {first}") 