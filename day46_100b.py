# john = {"daysCompleted": 46, "streak": 22}
# janet = {"daysCompleted": 21, "streak": 21}
# erica = {"daysCompleted": 75, "streak": 6}

# courseProgress = {"John":john, "Janet":janet, "Erica":erica}

# print(courseProgress["Erica"]["daysCompleted"])
# print(courseProgress["Janet"]["streak"])

# In Python, dictionary keys are case-sensitive. This means that if you use a capital letter for a key when you define the dictionary and then use a lowercase letter when you try to access the value associated with that key, it will not match and you will not be able to access the value.

# Here's an example:

my_dict = {"Key1": "Value1", "Key2": "Value2"}

# Accessing a key that is defined in the dictionary
# print(my_dict["Key1"]) # Output: "Value1"

# Accessing a key that is not defined in the dictionary
# print(my_dict["key1"]) # Output: KeyError: "key1"
# It's the same for nested dictionaries. If keys defined in nested dictionaries not matching with the key you're trying to access you will get KeyError

# 
# my_dict = {"Key1": {"Key2": "Value1"}}
# print(my_dict["Key1"]["Key2"]) # Output: "Value1"
# print(my_dict["Key1"]["key2"]) # Output: KeyError: "key2"
# It's a good practice to make sure that your keys are consistently spelled and cased when working with dictionaries, especially when dealing with nested dictionaries.

# Also you can use python built-in method get() to avoid the error and return a default value if the key is not present in the dictionary,

# Copy code
# print(my_dict.get("Key1", {}).get("key2")) 
# Output: None