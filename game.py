from models.calculate import Calculate

def main() -> None:
    points: int = 0
    play(points)

def play(points: int) -> None:
    difficulty: int = int(input('Choose difficulty level [1,2,3 ou 4]: '))

    calc: Calculate = Calculate(difficulty)

    print('What is the result for this operation: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        points += 1
        print(f'You have {points} point(s).')

    again: int = int(input('Do you want to continue? [1 - yes, 0 - no]'))

    if again:
        play(points)
    else:
        print(f'You ended up with {points} point(s).')
        print('See you later!')

if __name__ == '__main__':
    main()