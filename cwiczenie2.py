def task_1():
    print("\n=== Zadanie 1 ===")
    try:
        number = input("Podaj liczbę: ")
        number = int(number)
        
        if number % 2 == 0:
            print(f"Liczba {number} jest parzysta.")
        else:
            print(f"Liczba {number} jest nieparzysta.")
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać liczbę całkowitą.")


def task_2():
    print("\n=== Zadanie 2 ===")
    try:
        number = input("Podaj liczbę: ")
        number = float(number)
        
        if number > 0:
            print(f"Liczba {number} jest dodatnia.")
        elif number < 0:
            print(f"Liczba {number} jest ujemna.")
        else:
            print("Liczba jest równa zero.")
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać liczbę.")


def task_3():
    print("\n=== Zadanie 3 ===")
    try:
        year = input("Podaj rok: ")
        year = int(year)
        
        if year <= 0:
            print("Błąd: Rok musi być liczbą dodatnią.")
        else:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(f"Rok {year} jest rokiem przestępnym.")
            else:
                print(f"Rok {year} nie jest rokiem przestępnym.")
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać rok jako liczbę całkowitą.")


def task_4():
    print("\n=== Zadanie 4 ===")
    try:
        number = input("Podaj liczbę: ")
        number = int(number)
        
        if number % 2 == 0:
            print(f"Liczba {number} jest parzysta.")
        else:
            print(f"Liczba {number} jest nieparzysta.")
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać liczbę całkowitą.")


def task_5():
    print("\n=== Zadanie 5 ===")
    try:
        age = input("Podaj wiek: ")
        age = int(age)
        
        if age < 0:
            print("Błąd: Wiek nie może być liczbą ujemną.")
        elif age >= 18:
            print(f"Osoba w wieku {age} lat jest pełnoletnia.")
        else:
            print(f"Osoba w wieku {age} lat jest niepełnoletnia.")
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać wiek jako liczbę całkowitą.")


def task_6():
    print("\n=== Zadanie 6 ===")
    try:
        grade = input("Podaj ocenę (1-5): ")
        grade = int(grade)
        
        if grade == 5:
            print("Ocena 5 - bardzo dobry")
        elif grade == 4:
            print("Ocena 4 - dobry")
        elif grade == 3:
            print("Ocena 3 - dostateczny")
        elif grade == 2:
            print("Ocena 2 - dopuszczający")
        elif grade == 1:
            print("Ocena 1 - niedostateczny")
        else:
            print(f"Błąd: Ocena {grade} jest nieprawidłowa. Podaj ocenę w skali 1-5.")
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać ocenę jako liczbę całkowitą.")


def task_7():
    print("\n=== Zadanie 7 ===")
    try:
        number = input("Podaj liczbę: ")
        number = int(number)
        
        if number < 2:
            print(f"Liczba {number} nie jest liczbą pierwszą.")
        elif number == 2:
            print(f"Liczba {number} jest liczbą pierwszą.")
        else:
            is_prime = True
            i = 2
            while i * i <= number:
                if number % i == 0:
                    is_prime = False
                    break
                i += 1
            
            if is_prime:
                print(f"Liczba {number} jest liczbą pierwszą.")
            else:
                print(f"Liczba {number} nie jest liczbą pierwszą.")
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać liczbę całkowitą.")


def main():
                task_1()    
                task_2()       
                task_3()      
                task_4()      
                task_5()    
                task_6()       
                task_7()
          


if __name__ == "__main__":
    main()
