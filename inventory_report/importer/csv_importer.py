import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(caminho_para_o_arquivo):
        if not caminho_para_o_arquivo.endswith("csv"):
            raise ValueError("Arquivo inválido")

        with open(caminho_para_o_arquivo, "r", encoding="utf-8") as file:
            return list(csv.DictReader(file))
