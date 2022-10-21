def solution(phone_book):
    phone_book = sorted(phone_book)
    print(phone_book)
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            return False

    return True