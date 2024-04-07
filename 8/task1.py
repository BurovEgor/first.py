my_img = ('1920', '1080')

info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else "Incorrect image formatting"

print(info)


if len(my_img) == 2:
    info_re = f"{my_img[0]}x{my_img[1]}"
else:
    print("Incorrect image formatting")

print(info_re)


if len(info_re) > 79:
    print("String is long")
else:
    print("String is short")