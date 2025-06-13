

def input_error(func):
    """
    декоратор який обробляє помилки при вводі юзера
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "key error."
        except IndexError:
            return "Enter the argument for the command."
    return inner



@input_error
def parse_input(user_input):
    """
    функція приймає аргументи з введеного юзером рядка, розбиває їх за пробілом, 
    переводить в нижній регістр і повертає
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    """
    функція додає контакт у список контактів
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    функція змінює контакт у список контактів
    """
    name, phone = args
    contacts[name] = phone
    return "Contact modified."

@input_error
def show_phone(args, contacts):
    """
    функція показує телефон заданого контакта
    """
    name = args[0]
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    return f"Phone of {name} is {contacts[name]}"

@input_error
def show_all(contacts):
    """
    функція показує всі телефони всіх контактів
    """
    list_of_contacts = []
    for name in contacts:
        list_of_contacts.append(f"Phone of {name} is {contacts[name]}")
    return list_of_contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print('All the commands: "hello" "add" "change" "phone" "all" "close"/"exit"')
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))  
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            contact_list = show_all(contacts)
            for contact in contact_list:
                print(contact)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
