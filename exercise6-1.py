text = input('What text would you like to wrap ')
first_wrap = '###'

def wrap_text(text_2_wrap, wrap):
    return wrap + text + wrap[::-1]


print(wrap_text(text, '###'))
print(wrap_text(text, '---===###'))
# def wrap_text2(wrap_text1):
#     wrap_text2 = str(second_wrap + wrap_text1 + second_wrap)
#     return wrap_text2
# def wrap_text3(wrap_text1):
#     wrap_text2 = str(third_wrap + wrap_text2 + third_wrap)
#     return wrap_text3


# def wrap_text2(text_2_wrap, 2nd_wrap):