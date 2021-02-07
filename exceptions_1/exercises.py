def case_1():
    list_of_numbers = [1, 2, 31, 54, 32]

    print("Case_1 before")
    try:
        result = list_of_numbers[5]
    except IndexError as ie:
        print(f'1. Exceptions caught {ie.args}')
    except Exception as ex:
        print(f'2. Exception cought{ex.args}')
    print("Case_1 after")

    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as e:
        print(f'3. Exceptions caught {e.args}')


def case_2(name: str):
    if len(name) <= 0:
        raise ValueError('String is empty')
    print(f'Given name is {name}')

