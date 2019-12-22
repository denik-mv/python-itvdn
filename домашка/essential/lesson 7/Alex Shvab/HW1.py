import url_work


while True:
    print("""Select operation:
    1. Take short link
    2. Take original link
    3. Exit""")
    choose = int(input("> "))
    if choose == 1:
        enter_full_url = input("Enter your url: ")
        print("Short link: ", url_work.cut_link(enter_full_url))
    elif choose == 2:
        short_link = input("Enter your short link: ")
        print("Full link: ", url_work.full_link(short_link))
    else:
        print("Exit")
        break

if __name__ == "__main__":
    main()