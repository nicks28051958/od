import timeit

class Graph:
    """
    Класс Graph реализует граф с методами для добавления вершин и рёбер,
    а также методом обхода графа в глубину (DFS).
    """

    def __init__(self):
        # Инициализируем пустой словарь для хранения смежных вершин
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Добавляет вершину в граф.
        :param vertex: добавляемая вершина.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Добавляет ребро между двумя вершинами.
        :param vertex1: первая вершина.
        :param vertex2: вторая вершина.
        """
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        else:
            print(f"Одна из вершин {vertex1} или {vertex2} не найдена в графе")

    def dfs(self, start, visited=None):
        """
        Выполняет обход графа в глубину (DFS), начиная с указанной вершины.
        :param start: начальная вершина для DFS.
        :param visited: множество для хранения посещённых вершин.
        :return: список посещённых вершин.
        """
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in self.adjacency_list[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Пример использования графа и замера времени
if __name__ == "__main__":
    # Создаем экземпляр графа
    graph = Graph()

    # Измеряем время добавления вершин
    vertex_time = timeit.timeit(lambda: [graph.add_vertex(v) for v in ['A', 'B', 'C', 'D', 'E']], number=1)
    print(f"Время на добавление вершин: {vertex_time:.5f} секунд")

    # Измеряем время добавления рёбер
    edge_time = timeit.timeit(lambda: [graph.add_edge('A', 'B'), graph.add_edge('A', 'C'),
                                       graph.add_edge('B', 'D'), graph.add_edge('C', 'D'),
                                       graph.add_edge('D', 'E')], number=1)
    print(f"Время на добавление рёбер: {edge_time:.5f} секунд")

    # Измеряем время выполнения DFS
    dfs_time = timeit.timeit(lambda: graph.dfs('A'), number=1)
    print(f"Время выполнения DFS: {dfs_time:.5f} секунд")
