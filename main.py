from classes import Station, Metro

original_network = Metro()
colors = ['red', 'green']

while True:
    file = input("Enter the name of the file that contains the Metro network: ")
    try:
        original_network.load_network(file)
        break
    except Exception as e:
        print('File not found. Check that your file exists please :).')

original_network.load_network(file)
# original_network.print_graph()
stations = original_network.print_stations()

for index, station in enumerate(stations, start=0):
    print (str([index]), station)

while True:
    try:
        start = int(input("Enter the number of the starting station: "))
        if 0 <= start < len(stations):
            break
        else:
            print("You must enter one of the numbers above ")
    except Exception as e:
        print(f'You must enter a number between 0 and {len(stations) - 1}')

while True:
    try:
        goal = int(input("Enter the number of the end station: "))
        if 0 <= goal < len(stations):
            break
        else:
            print("You must enter one of the numbers above ")
    except Exception as e:
        print(f'You must enter a number between 0 and {len(stations) - 1}')

while True:
    try:
        choose_color = input("Would you like to choose a train color? [Y/N] ")
        if choose_color == 'Y' or choose_color == 'N':
            break
        else:
            print('You must enter Y or N')
    except Exception as e:
        print('You must enter Y or N')

if choose_color == 'Y':

    for index, color in enumerate(colors, start=0):
        print (str([index]), color)

    while True:
        try:
            index_color = int(input("Enter the color of the train "))
            if 0 <= index_color < 2:
                break
            else:
                print("You must enter one of the numbers above ")
        except Exception as e:
            print(f'You must enter a number between 0 and 1')
    color = colors[index_color]

else:
    color = "white"

original_network.update_network(color)
shortest_path = original_network.find_shortest_path(stations[start], stations[goal], color, True)


# file = "easy.txt"
# start = 'A'
# goal = 'F'
# shortest_path = original_network.find_shortest_path(start, goal, color, True)


def test_cases(number, train_color, expected_output, start, goal):
    file = "easy.txt"
    network = Metro()
    network.load_network(file)
    network.update_network(train_color)
    path_list = None
    shortest_path = network.find_shortest_path(start, goal, train_color, True)
    if shortest_path != None:
        path_list = [x.name for x in shortest_path]
    print(f"CASO {number}:", path_list == expected_output, "\n")


if __name__ == '__main__':
    print("\n------------ CASOS DE PRUEBA ----------------\n")
    # CASO 1 Tren: Rojo Estacion Inicial: Blanca Estacion Final: Blanca
    print("CASO 1 Tren: Rojo Estacion Inicial: Blanca Estacion Final: Blanca")
    expected = ['A', 'B', 'C', 'H', 'F']
    test_cases(1, "red", expected, 'A', 'F')

    # CASO 2 Tren: Verde Estacion Inicial: Blanca Estacion Final: Blanca
    print("CASO 2 Tren: Verde Estacion Inicial: Blanca Estacion Final: Blanca")
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    test_cases(2, "green", expected, 'A', 'F')

    # CASO 3 Tren: Blanco Estacion Inicial: Blanca Estacion Final: Blanca
    print("CASO 3 Tren: Blanco Estacion Inicial: Blanca Estacion Final: Blanca")
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    test_cases(3, "white", expected, 'A', 'F')

    # CASO 4 Tren: Blanco Estacion Inicial: Blanca Estacion Final: Roja
    print("CASO 4 Tren: Blanco Estacion Inicial: Blanca Estacion Final: Roja")
    expected = ['A', 'B', 'C', 'G', 'H']
    test_cases(4, "white", expected, 'A', 'H')

    # CASO 5 Tren: Blanco Estacion Inicial: Blanca Estacion Final: Verde
    print("CASO 5 Tren: Blanco Estacion Inicial: Blanca Estacion Final: Verde")
    expected = ['A', 'B', 'C', 'G']
    test_cases(5, "white", expected, 'A', 'G')

    # CASO 6 Tren: Rojo Estacion Inicial: Blanca Estacion Final: Verde
    print("CASO 6 Tren: Rojo Estacion Inicial: Blanca Estacion Final: Verde")
    expected = None
    test_cases(6, "red", expected, 'A', 'G')

    # CASO 7 Tren: Verde Estacion Inicial: Roja Estacion Final: Verde
    print("CASO 7 Tren: Verde Estacion Inicial: Roja Estacion Final: Verde")
    expected = None
    test_cases(7, "green", expected, 'H', 'G')

    # CASO 8 Tren: Rojo Estacion Inicial: Blanca Estacion Final: Verde
    print("CASO 8 Tren: Rojo Estacion Inicial: Blanca Estacion Final: Verde")
    expected = None
    test_cases(8, "red", expected, 'A', 'G')
