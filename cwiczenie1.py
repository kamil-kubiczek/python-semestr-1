def task_1():
    print("\n=== Zadanie 1 ===")
    try:
        first_name = input("Podaj swoje imię: ")
        last_name = input("Podaj swoje nazwisko: ")
        
        # Validate first name
        if not first_name or not first_name.strip():
            print("Błąd: Imię nie może być puste.")
            return
        
        # Validate last name
        if not last_name or not last_name.strip():
            print("Błąd: Nazwisko nie może być puste.")
            return
        
        # Remove unnecessary spaces
        first_name = first_name.strip()
        last_name = last_name.strip()
        
        # Check if first name has proper format
        if not all(c.isalpha() or c.isspace() or c == '-' for c in first_name):
            print("Błąd: Imię powinno zawierać tylko litery.")
            return
        
        # Check if last name has proper format
        if not all(c.isalpha() or c.isspace() or c == '-' for c in last_name):
            print("Błąd: Nazwisko powinno zawierać tylko litery.")
            return
        
        # Check minimum length
        if len(first_name) < 2:
            print("Błąd: Imię jest zbyt krótkie (minimum 2 znaki).")
            return
        
        if len(last_name) < 2:
            print("Błąd: Nazwisko jest zbyt krótkie (minimum 2 znaki).")
            return
        
        print(f"Imię: {first_name}")
        print(f"Nazwisko: {last_name}")
    except Exception as e:
        print(f"Błąd: {e}")


def task_2():
    print("\n=== Zadanie 2 ===")
    try:
        num1 = input("Podaj pierwszą liczbę: ")
        num2 = input("Podaj drugą liczbę: ")
        
        num1 = float(num1)
        num2 = float(num2)
        
        sum_result = num1 + num2
        difference = num1 - num2
        product = num1 * num2
        
        print(f"Suma: {num1} + {num2} = {sum_result}")
        print(f"Różnica: {num1} - {num2} = {difference}")
        print(f"Iloczyn: {num1} * {num2} = {product}")
        
        if num2 != 0:
            quotient = num1 / num2
            print(f"Iloraz: {num1} / {num2} = {quotient}")
        else:
            print("Iloraz: Nie można dzielić przez zero")
            
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać liczby.")
    except Exception as e:
        print(f"Błąd: {e}")


def task_3():
    print("\n=== Zadanie 3 ===")
    try:
        celsius = input("Podaj temperaturę w stopniach Celsjusza: ")
        celsius = float(celsius)
        
        fahrenheit = (celsius * 9/5) + 32
        
        print(f"{celsius}°C = {fahrenheit}°F")
        
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać liczbę.")
    except Exception as e:
        print(f"Błąd: {e}")


def task_4():
    print("\n=== Zadanie 4 ===")
    try:
    
        num1 = input("Podaj pierwszą liczbę: ")
        
        num2 = input("Podaj drugą liczbę: ")
        
        num1 = float(num1)
        num2 = float(num2)
        

        sum_result = num1 + num2
        

        print(f"Suma {num1} + {num2} = {sum_result}")
        
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Proszę podać liczby.")
    except Exception as e:
        print(f"Błąd: {e}")


def task_5():
    print("\n=== Zadanie 5 ===")
    try:
      
        width = input("Podaj szerokość prostokąta: ")
        
      
        height = input("Podaj wysokość prostokąta: ")
        
       
        width = float(width)
        height = float(height)
        
     
        if width <= 0 or height <= 0:
            print("Błąd: Wymiary prostokąta muszą być liczbami dodatnimi.")
            return
        
    
        area = width * height
        
      
        print(f"Pole prostokąta o wymiarach {width} x {height} = {area}")
        
    except ValueError:
     
        print("Błąd: Podano nieprawidłową wartość. Proszę podać liczby.")
    except Exception as e:

        print(f"Błąd: {e}")


def task_6():

    print("\n=== Zadanie 6 ===")
    try:

        first_name = input("Podaj swoje imię: ")
        
 
        last_name = input("Podaj swoje nazwisko: ")
        
 
        if not first_name or not first_name.strip():
            print("Błąd: Imię nie może być puste.")
            return
        
      
        if not last_name or not last_name.strip():
            print("Błąd: Nazwisko nie może być puste.")
            return
        
     
        first_name = first_name.strip()
        last_name = last_name.strip()
        
        # Check if first name contains only letters and spaces
        if not all(c.isalpha() or c.isspace() or c == '-' for c in first_name):
            print("Błąd: Imię powinno zawierać tylko litery.")
            return
        
        # Check if last name contains only letters, spaces and hyphens
        if not all(c.isalpha() or c.isspace() or c == '-' for c in last_name):
            print("Błąd: Nazwisko powinno zawierać tylko litery.")
            return
        
        # Check if they are strings
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            print("Błąd: Imię i nazwisko muszą być ciągami znaków.")
            return
        
        print(f"Nazwisko, Imię: {last_name}, {first_name}")
        
    except Exception as e:
        print(f"Błąd: {e}")


def main():        
                task_1()       
                task_2()         
                task_3()        
                task_4()       
                task_5()       
                task_6()
        


if __name__ == "__main__":
    main()
