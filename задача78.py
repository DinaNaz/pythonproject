previous_word = input()
while True:
    current_word = input()
    if current_word[0] != previous_word[-1]:
        print(current_word)
        break
    previous_word = current_word