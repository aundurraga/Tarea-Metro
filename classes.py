import networkx as nx
from matplotlib import pyplot as plt
from termcolor import colored

from functions import define_train_color


class Station:
    def __init__(self, name):
        self.name = name
        self.color = 'white'  # red, green, white
        self.connections = []

    def connect(self, station):
        self.connections.append(station)


class Metro:
    def __init__(self):
        self.stations = dict()

    def _create_node(self, name):
        station = self.stations.get(name)
        if station is None:
            station = Station(name)
            self.stations[name] = station
        return station

    def add_connection(self, start, next, color):
        start_station = self._create_node(start)
        start_station.color = color
        next_station = self._create_node(next)
        start_station.connect(next_station)
        next_station.connect(start_station)

    def load_network(self, path):

        with open('tests/' + path, 'r') as file:
            for line in file:
                station_info, next = line.strip().split(':')
                station, color = station_info.split(',')
                if color == 'R':
                    station_color = 'red'
                elif color == 'G':
                    station_color = 'green'
                else:
                    station_color = 'white'
                self.add_connection(station.upper(), next, station_color)

    def update_network(self, color):
        for station in list(self.stations.keys()):
            station_colors = define_train_color(color)
            for next_station in list(self.stations.keys()):
                path = self.find_shortest_path(station, next_station, color, False)
                next_station = self.stations.get(next_station)
                if type(path) == list:
                    if path[0].color in station_colors and path[-1].color in station_colors and len(path) > 2:
                        if all(x.color not in station_colors for x in path[1:-1]):
                            path[0].connect(next_station)

    def find_shortest_path(self, start, goal, color, print_function):
        visited = []
        if start == goal:
            if print_function:
                print("The start and end station are the same!")
            return
        start = self.stations.get(start)
        goal = self.stations.get(goal)
        travelled_paths = [[start]]
        station_colors = define_train_color(color)
        if color in ['green', 'red'] and start.color not in station_colors:
            if print_function:
                print(f"There is no path for the {color} train that connects {start.name} with {goal.name}.")
                print(
                    f"You can`t ride a {color} train in a {start.color} station, please wait for a white "
                    f"or {start.color} train.")

            return None

        if color in ['green', 'red'] and goal.color not in station_colors:
            if print_function:
                print(f"There is no path for the {color} train that connects {start.name} with {goal.name}.")

                print(f"You can`t get to a {goal.color} station with a {color} train, please wait for a white train.")

            return None

        while len(travelled_paths):
            current_path = travelled_paths.pop(0)
            current_station = current_path[-1]
            if current_station not in visited:
                visited.append(current_station)
                connections = current_station.connections
                for neighbour_station in connections:
                    travelled_paths.append(list(current_path) + [neighbour_station])
                    if neighbour_station.name == goal.name:
                        if print_function:
                            print(
                                f"The shortest path for the {color} train that gets from {start.name} "
                                f"to {goal.name} is:")
                            print(' -> '.join(x.name for x in travelled_paths[-1]))
                        return travelled_paths[-1]
        if print_function:
            print('There is no path')
        return None

    def print_stations(self):
        stations = list(self.stations.keys())
        print(f"The stations in the Metro network are: {' - '.join(stations)}")
        return stations

    def print_connections(self):
        for station in self.stations:
            print(colored(f"{station}:", self.stations[station].color),
                  ','.join(x.name for x in self.stations[station].connections))

    def return_connections(self):
        connections_list = []
        for station in self.stations:
            for connection in self.stations[station].connections:
                connections_list.append((station, connection.name))
        return connections_list

    def print_graph(self):  # Source: https://www.python-course.eu/networkx.php
        graph = nx.Graph()
        connections = self.return_connections()
        graph.add_nodes_from(list(self.stations.keys()))
        graph.add_edges_from(connections)
        nx.draw(graph, with_labels=True, node_color=[self.stations[node].color for node in graph])
        plt.savefig("graph_images/graph_hard.png")  # save as png
