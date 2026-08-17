from structures.deque import Deque

def palindrome_checker(string: str):
    deque = Deque()
    for s in string:
        deque.addFront(s)

    while deque.size() > 1:
        first = deque.removeFront()
        last = deque.removeRear()
        if first != last:
            return False

    return True


def main():
    print(palindrome_checker("madam"))
    print(palindrome_checker("root"))

if __name__ == "__main__":
    main()
