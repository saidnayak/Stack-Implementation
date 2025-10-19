# Stack Implementation in Python

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"{item} pushed onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Nothing to pop.")
        else:
            removed = self.items.pop()
            print(f"Popped item: {removed}")

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print(f"Top item: {self.items[-1]}")

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements:", self.items)


def main():
    stack = Stack()

    while True:
        print("\n--- Stack Operations ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            element = input("Enter element to push: ")
            stack.push(element)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
