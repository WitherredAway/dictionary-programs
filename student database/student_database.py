import time


BORDER = "-" * 30


def format_dict(dictionary, *, indent="  "):
    """Function to nicely format the keys and values of a dictionary"""

    # This list comprehension is used to format each key and value of the dictionary
    return "\n".join(
        [
            f"{indent}{key.title() if isinstance(key, str) else key}: {value}"
            for key, value in dictionary.items()
        ]
    )


data = {0: {"Name": "Souvic Das", "Class": "XI", "Section": "SC-1"}}

while True:
    time.sleep(1)
    option = input(
        f"""
{BORDER}
1. Add Student Data
2. View Student Data
3. Remove Student Data
{BORDER}
Please choose an option: """
    )

    try:
        option = int(option)
    except ValueError:
        break

    if option == 1:
        _id = len(data)  # ID of the student
        name = input("Name: ")
        _class = input("Class: ")
        section = input("Section: ")

        data[_id] = {"Name": name, "Class": _class, "Section": section}
        print(f"Added student #{_id} to database.")

    elif option == 2:
        _id = input("Please input ID of student to view. Leave empty to view all: ")

        if len(_id) == 0:
            for std in data.values():
                print(format_dict(std))
                print()
        else:
            _id = int(_id)
            try:
                student_data = data[_id]
            except KeyError:
                print("Student does not exist in database.")
                continue
            print(format_dict(student_data))

    elif option == 3:
        _id = int(input("Please input ID of student to remove: "))

        try:
            del data[_id]
        except KeyError:
            print("Student does not exist in database.")
        else:
            print(f"Deleted student #{_id} from database.")
