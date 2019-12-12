class NumberNotInRange(Exception):
    """User-defined exception."""
    pass


class ListNotDefined(Exception):
    """User-defined exception."""
    pass


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


# This block code will ask us numbers and append it into a list until we introduce a negative number, then it will
# return the list. Also the function covers the ValueError with an error message. """
def read_real():
    numlist = []
    while True:
        try:
            temp = float(input("Introduce un numero real positivo: "))
            if temp >= 0:
                numlist.append(temp)
            if temp < 0:
                print("Lista definida: ", numlist)
                return numlist
        except ValueError:
            print("¡Introduce solo numeros!")


# This block calculates the sum of the list defined in the read_real(function).
def sum_read_real(real_list):
    try:
        if len(real_list) <= 0:
            raise ListNotDefined
    except ListNotDefined:
        print("")

    return sum(real_list)


# This block search the max value of the list defined in the read_real(function).
def search_max_in_list(real_list):
    return max(real_list)


# This block search the min value of the list defined in the read_real(function).
def search_min_in_list(real_list):
    return min(real_list)


# This block will calculate the travel of the list defined in the read_real(function).
def calculate_travel_in_list(l_max, l_min):
    return l_max - l_min


# This block will calculate the average of the list defined in the read_real(function).
def calculate_average_in_list(sum_list, real_list):
    return sum_list / len(real_list)


while True:
    option = show_menu()
    if option == 1:
        read_real()
# defined_list = read_real()
# print(defined_list)
#
# list_sum = sum_read_real(defined_list)
# print(list_sum)
#
# list_max = search_max_in_list(defined_list)
# print(list_max)
#
# list_min = search_min_in_list(defined_list)
# print(list_min)
#
# list_travel = calculate_travel_in_list(list_max, list_min)
# print(list_travel)
#
# list_average = calculate_average_in_list(list_sum, defined_list)
# print(list_average)
