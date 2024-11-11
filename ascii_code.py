def to_upper_case(my_str):
    my_str_2 = ""
    for charactor in my_str:
        converted  =chr(ord(charactor)-32)
        my_str_2 = my_str_2 + converted
        return my_str_2
        

print (to_upper_case("name"))