import csv
import json
from typing import List

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(caminho_para_o_arquivo: str, tipo_de_relatorio: str):
        dados_dos_produtos: List[dict] = []

        with open(caminho_para_o_arquivo, "r", encoding="utf-8") as file:
            if caminho_para_o_arquivo.endswith("csv"):
                dados_dos_produtos = list(csv.DictReader(file))
            elif caminho_para_o_arquivo.endswith("json"):
                dados_dos_produtos = json.load(file)
            elif caminho_para_o_arquivo.endswith("xml"):
                dados_do_xml = file.read()
                dados_dos_produtos = xmltodict.parse(
                    dados_do_xml
                )["dataset"]["record"]

        if tipo_de_relatorio == "simples":
            return SimpleReport.generate(dados_dos_produtos)
        elif tipo_de_relatorio == "completo":
            return CompleteReport.generate(dados_dos_produtos)
