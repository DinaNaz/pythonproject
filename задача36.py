while True:
    password = input()
    
    if len(password) < 8:
        print("Слишком короткий!")
        continue
        
    if "123" in password:
        print("Содержит 123!")
        continue
        
    password_confirm = input()
    if password != password_confirm:
        print("Пароли не совпадают!")
        continue
        
    print("OK")
    break
