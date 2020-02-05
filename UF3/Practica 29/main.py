""" Estas dos funciones lo que hacen es comprobar que el archivo exista, si no lo hace simplemente crean uno nuevo y le
 añaden contenido necesario. """


def check_cara_file():
    try:
        cara_file = open('Cara.txt', 'r')
    except FileNotFoundError:
        cara_file = open('Cara.txt', 'w')
        cara_file.write('ALFKI||Alfredo Futterkiste||Obere Str. 57||Berlín\n')
        cara_file.write('ANATR||Ana Trujillo Emparedados||Avda. de la Constitución 2222||México D.F.\n')
        cara_file.write('BLONP||Blondel père et fils||24, place Kléber||Estrasburgo\n')
        cara_file.write('BOLID||Bolido Comidas preparadas||C/ Araquil, 67||Madrid\n')
    finally:
        pass
    cara_file.close()


def check_dura_file():
    try:
        dura_file = open('Dura.txt', 'r')
    except FileNotFoundError:
        dura_file = open('Dura.txt', 'w')
        dura_file.write('ANTON||Antonio Moreno Taquería||Mataderos  2312||México D.F.\n')
        dura_file.write('AROUT||Around the Horn||120 Hanover Sq.||Londres\n')
        dura_file.write('BURGS||Berglunds snabbköp||Berguvsvägen  8||Lulea\n')
        dura_file.write('BLAUS||Blauer See Delikatessen||Forsterstr. 57||Mannheim\n')
        dura_file.write('BVBEV||BVs Beverages||Fauntleroy Circus||Londres\n')
    finally:
        pass
    dura_file.close()


def get_lines_from_files():
    lines = []
    cara_file = open('Cara.txt', 'r')
    dura_file = open('Dura.txt', 'r')
    for line in cara_file:
        lines.append(line.split('||'))
    cara_file.close()
    for line in dura_file:
        lines.append(line.split('||'))
    dura_file.close()
    return lines


def list_sort(lines):
    company_names = []
    for line in lines:
        company_names.append(line[1].upper())
    company_names.sort()
    return company_names


def input_in_file(companies, file_lines):
    caradura_file = open('CaraDura.txt', 'w')
    for company in companies:
        for position in file_lines:
            for element in position:
                if company == element.upper():
                    write_line_in_file(position, caradura_file)
    caradura_file.close()


def write_line_in_file(list_to_input, file):
    for element in list_to_input:
        file.write('||')
        file.write(element)
    return 'pass'


check_cara_file()
check_dura_file()
all_lines = get_lines_from_files()
all_companies = list_sort(all_lines)
input_in_file(all_companies, all_lines)
