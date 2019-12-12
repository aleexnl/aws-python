# Here we define the custom user exceptions, to have more traceability at debugging code.


class NumberNotInRange(Exception):
    """ User-defined exception. """
    pass


class ListNotDefined(Exception):
    """ User-defined exception. """
    pass


# This function code will print a menu and ask you an option and covers the exceptions against numbers not in the menu
# and introducing some weird characters instead of an integer.
def show_menu():
    while True:
        print("\nMENU:")
        print("1.\tDefinir lista\n"
              "2.\tCalcular el recorrido\n"
              "3.\tCalcular la media\n"
              "4.\tCalcular la variancia\n"
              "5.\tSalir del programa\n")
        try:
            opc = int(input("Introduce una opción: "))
            if opc not in range(1, 6):
                raise NumberNotInRange
            if opc in range(1, 6):
                return opc
        except ValueError:
            print("¡Introduce solo numeros!")
        except NumberNotInRange:
            print("¡El numero introducido no esta en el rango!")


# This function code will ask us numbers and append it into a list until we introduce a negative number, then it will
# return the list. Also the function covers the ValueError with an error message. """
def define_real_list():
    numlist = []
    while True:
        try:
            temp = float(input("Introduce un numero real positivo: "))
            if temp >= 0:
                numlist.append(temp)
            if temp < 0:
                if len(numlist) > 0:
                    print("Lista definida: ", numlist, "\n")
                    return numlist
                if len(numlist) == 0:
                    raise ListNotDefined
        except ValueError:
            print("¡Introduce solo numeros!")
        except ListNotDefined:
            print("¡No has definido la lista!")


# This function calculates the sum of the list defined in the read_real(function).
def sum_read_real(real_list):
    return sum(real_list)


# This function search the max value of the list defined in the read_real(function).
def search_max_in_list(real_list):
    return max(real_list)


# This function search the min value of the list defined in the read_real(function).
def search_min_in_list(real_list):
    return min(real_list)


# This function will calculate the travel of the list defined in the read_real(function).
def calculate_travel_in_list(l_max, l_min):
    return l_max - l_min


# This function will calculate the average of the list defined in the read_real(function).
def calculate_average_in_list(sum_list, real_list):
    return sum_list / len(real_list)


# Define variable using the functions, for further uses.
defined_list = define_real_list()  # Function to define the list.
list_sum = sum_read_real(defined_list)  # Function to get the sum of all the list.
average = calculate_average_in_list(list_sum, defined_list)  # Function to get the average.
E = 0  # Simple variable.
# This is an infinite loop to cover the options for the menu, you have five different possibilities.
while True:
    try:
        option = show_menu()  # Call the menu.
        # If and elif to check the result of the option.
        if option == 1:  # Option to define the list.
            defined_list = define_real_list()
        elif option == 2:  # Option to calculate the travel of the list.
            max_num = search_max_in_list(defined_list)
            min_num = search_min_in_list(defined_list)
            print("Recorrido de la lista: ", calculate_travel_in_list(max_num, min_num))
        elif option == 3:  # Option to calculate the average.
            print("Media de la lista: ", average)
        elif option == 4:  # Option to calculate the variance.
            for value in defined_list:
                E = E + ((value - average)**2)
            print("Variancia: ", E / (len(defined_list) - 1))
        elif option == 5:  # Finish the program
            print("¡Hasta la proxima!")
            break
    except NumberNotInRange:
        print("¡El numero introducido no esta en el rango!")
