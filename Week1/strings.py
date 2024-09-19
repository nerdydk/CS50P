value = input("Hey Can you please tell, Whats your name? ")

#this functions removes unnecessary spaces fromn the output, here name will be the str and strip will be a strip function
value = value.strip() 

# this function capitalizes the output, no matter what the user inputs
value = value.capitalize()

print(f"Hello {value}")


'''
so say a new string method, instead of value = value.capitalize() which just capitalizes the first letter of the first word, we use
value = value.title() , now this will capitalize first letter of all the words, user inputs

Lets try this once.
'''

name = input("Hey can you please tell your full name? ")

name = name.strip() 

name = name.title()

print(f"Hello {name}")


''' 

other methods we can also do this
name = name.strip().title()
or 
name = input("Hey whats ur name buddy? ").strip().title()

'''

name = input("Hey can you please tell your full name? ").strip().title()

#Split first and second name

print(f"Hello {name}")
