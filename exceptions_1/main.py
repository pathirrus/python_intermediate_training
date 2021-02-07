from exceptions_1.exercises import case_1, case_2


def main():
    print('Start up')

    case_1()

    try:
        case_2("")
    except ValueError as ve:
        print(f'Value error {ve.args}')

    print("Finish")


if __name__ == '__main__':
    main()
