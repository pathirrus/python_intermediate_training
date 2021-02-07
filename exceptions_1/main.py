from exceptions_1.exercises import case_1, case_2, case_3, case_4


def main():
    print('Start up')

    case_1()

    try:
        case_2("")
    except ValueError as ve:
        print(f'Value error {ve.args}')

    print(case_3(10, 0))

    dictionary = {
        'products': ['masło', 'chleb']
    }
    case_4(dictionary)


    print("Finish")


if __name__ == '__main__':
    main()
