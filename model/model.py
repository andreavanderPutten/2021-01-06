import networkx as nx

from database.DAO import DAO
from database.DB_connect import DBConnect
class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def creaGrafo(self):
        self.grafo.clear()
        geni_essenziali = DAO.getGeniEssenziali()
        self.grafo.add_nodes_from(geni_essenziali)
        iterazioni = DAO.getIterazioni()
        booleano = True
        for tupla in iterazioni :
            if tupla[0] in geni_essenziali :
    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)


