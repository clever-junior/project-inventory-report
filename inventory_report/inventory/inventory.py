from typing import List

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(caminho_para_o_arquivo: str, tipo_de_relatorio: str):
        produtos: List[dict] = []

        extensao_do_arquivo = caminho_para_o_arquivo.rsplit(".", 1)[-1]

        match extensao_do_arquivo:
            case "csv":
                produtos = CsvImporter().import_data(caminho_para_o_arquivo)
            case "json":
                produtos = JsonImporter().import_data(caminho_para_o_arquivo)
            case "xml":
                produtos = XmlImporter().import_data(caminho_para_o_arquivo)
            case _:
                raise ValueError("Arquivo inválido")

        if tipo_de_relatorio == "simples":
            return SimpleReport.generate(produtos)
        elif tipo_de_relatorio == "completo":
            return CompleteReport.generate(produtos)
        else:
            raise ValueError("Tipo de relatório inválido")
