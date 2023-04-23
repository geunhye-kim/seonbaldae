phone_book = {"John": "123-4567", "Jane": "234-5678", "Max": "345-6789"}


def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = "Cannot find the name in the phone book."
        name = yield phone_number


# 코루틴 객체 생성
search_coroution = search()
next(search_coroution)

# 검색 예시
result = search_coroution.send("John")
print(result)  # 123-4567

result = search_coroution.send("Jane")
print(result)  # 234-5678

result = search_coroution.send("Sarah")
print(result)  # Cannot find the name in the phone book.
