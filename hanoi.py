def hanoi(n, from_pole, to_pole, with_pole):
    if n == 1:
        print('moving disc', from_pole, 'to', to_pole)
        return
    hanoi(n-1, from_pole, with_pole, to_pole)
    print('moving disc', from_pole, 'to', to_pole)
    hanoi(n-1, with_pole, to_pole, from_pole)

# Driver code

hanoi(3, 'A', 'B', 'C')
print('\n')
hanoi(3, 'A', 'C', 'B')

