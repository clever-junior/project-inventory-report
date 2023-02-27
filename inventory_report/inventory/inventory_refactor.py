from typing import List

from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importador: Importer):
        self.dados: List[dict] = []
        self.importador = importador

    def __iter__(self):
        return InventoryIterator(self.dados)

    def import_data(self, caminho_para_o_arquivo: str, tipo_de_relatorio: str):
        self.dados.extend(
            self.importador.import_data(caminho_para_o_arquivo)
        )

        match tipo_de_relatorio:
            case "simples":
                return SimpleReport.generate(self.dados)
            case "completo":
                return CompleteReport.generate(self.dados)
            case _:
                raise ValueError("Tipo de relatório inválido")
