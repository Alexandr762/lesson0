calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    length = len(string)
    uppercase = string.upper()
    lowercase = string.lower()
    return length, uppercase, lowercase

def is_contains(string, list_to_search):
    for item in list_to_search:
        if string.lower() == item.lower():
            return True
    return False


for _ in range(11):
    count_calls()
    string_info("Привет")
    is_contains("привет", ["hello", "world"])

print(calls)
