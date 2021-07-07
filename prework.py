# question 1
# def hello_name(user_name):
#     print("Hello {}!".format(user_name.title()))
#     pritn("Hello {}!" your favorite languageis {}!".format(user_name.title()))

# hello_name('Gil')

# def hello_name():
#     user_name = input("enter your username: ")
#     print("Hello " + user_name + ".")


# hello_name()


# def max_num_in_list(a_list):
#     max = a_list[0]


# for num in a_list:
#     if num > max:
#         max = num
# print("max")

# max_num_in_list([15, 298, -3, 24354])


def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list)-1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
        return status


is_consecutive(1, 2, 3, 4, 5, 10, 11, 12)
