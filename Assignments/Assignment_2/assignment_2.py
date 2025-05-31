class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        if not curr:
            print("The list is empty.")
            return
        nodes = []
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(nodes))

    def delete_nth_node(self, n):
        if n < 1:
            print("Position must be 1 or greater.")
            return
        if not self.head:
            print("Cannot delete from an empty list.")
            return
        if n == 1:
            print(f"Deleting node with value {self.head.data} from position {n}")
            self.head = self.head.next
            return
        curr = self.head
        prev = None
        count = 1
        while curr and count < n:
            prev = curr
            curr = curr.next
            count += 1
        if not curr:
            print("Position out of range.")
            return
        print(f"Deleting node with value {curr.data} from position {n}")
        prev.next = curr.next

if __name__ == "__main__":
    my_list = LinkedList()
    while True:
        print("\nChoose an operation:")
        print("1. Add element")
        print("2. Print list")
        print("3. Delete nth node")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                data = int(input("Enter value to add: "))
                my_list.add(data)
                print(f"Added {data}.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == 2:
            print("Current list:")
            my_list.print_list()
        elif choice == 3:
            try:
                n = int(input("Enter the position of the node to delete (1-based index): "))
                my_list.delete_nth_node(n)
            except ValueError:
                print("Invalid input! Please enter a valid position.")
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please select from 1 to 4.")