import flet as ft
from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        geni = DAO.getGeni()

        self._view._dd_gene.options = list(map(lambda x: ft.dropdown.Option(x),geni))

    def handle_graph(self, e):
        self._model.creaGrafo()

        self._view.txtOut.controls.append(ft.Text(f"nodi: {self._model.grafoDetails()[0]}, archi {self._model.grafoDetails()[1]}"))
        self._view.update_page()

    def handle_geni_adiacenti(self, e):
        pass

    def handle_ingegneri(self, e):
        pass
    def handle_simulazione(self, e):
        pass