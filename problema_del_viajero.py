import networkx as nx

def create_transport_graph():
    """Crea un grafo que representa el sistema de transporte masivo local."""
    G = nx.DiGraph()
    # Añadir nodos y aristas (con pesos) al grafo
    G.add_edge('A', 'B', weight=1)
    G.add_edge('A', 'C', weight=2)
    G.add_edge('B', 'C', weight=1)
    G.add_edge('B', 'D', weight=3)
    G.add_edge('C', 'D', weight=1)
    G.add_edge('C', 'E', weight=5)
    G.add_edge('D', 'E', weight=2)
    return G

def find_shortest_path(graph, start, end):
    """Encuentra la ruta más corta desde start hasta end en el grafo."""
    return nx.dijkstra_path(graph, start, end, weight='weight')

def main():
    # Crear el grafo del sistema de transporte
    G = create_transport_graph()

    # Definir los puntos de inicio y fin
    start = 'A'
    end = 'E'

    # Encontrar la ruta más corta
    shortest_path = find_shortest_path(G, start, end)

    # Imprimir la ruta más corta
    print(f'La ruta más corta desde {start} hasta {end} es: {shortest_path}')

if __name__ == '__main__':
    main()