ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Simply replace second element in list
ft_list[1] = "World!"
# Must recreate the tuple because tuple are immutables
ft_tuple = (ft_tuple[0], "France!")
# Remove wrong element and add good one, sets do not guarantee an order
ft_set.remove("tutu!")
ft_set.add("Paris!")
# Replace the wrong value
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
