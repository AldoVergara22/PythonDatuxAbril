while True:
    print("Por favor eliga una opcion:")
    print("1. Dibujar un cuadrado en la consola")
    print("2.Identificar números pares en una lista. ")
    print("3. Print only adults from a list")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        size = int(input("Enter the size of the square: "))
        for i in range(size):
            for j in range(size):
                print('*', end=' ')
            print()
    elif choice == '2':
        numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
        for num in numbers:
            if num % 2 == 0:
                print(num)
    elif choice == '3':
        people = [[name, int(age)] for name, age in [input("Enter a name and age separated by a comma: ").split()]]
        for person in people:
            if person[1] >= 18:
                print(person[0])
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
