import csv
from typing import List

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(caminho_para_o_arquivo: str, tipo_de_relatorio: str):
        dados_dos_produtos: List[dict] = []

        with open(caminho_para_o_arquivo, 'r', encoding="utf-8") as file:
            dados_dos_produtos = list(csv.DictReader(file))

        if tipo_de_relatorio == "simples":
            return SimpleReport.generate(dados_dos_produtos)
        elif tipo_de_relatorio == "completo":
            return CompleteReport.generate(dados_dos_produtos)
