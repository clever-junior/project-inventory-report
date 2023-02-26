from collections import Counter
from typing import List

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(dados_dos_produtos: List[dict]) -> str:
        relatorio_simples: str = SimpleReport.generate(dados_dos_produtos)
        nomes_das_empresas: List[str] = []
        produtos_estocados_por_empresa = "Produtos estocados por empresa:\n"

        for produto in dados_dos_produtos:
            nomes_das_empresas.append(produto["nome_da_empresa"])

        contagem_das_empresas = Counter(nomes_das_empresas)

        for empresa, quantidade in contagem_das_empresas.items():
            produtos_estocados_por_empresa += f"- {empresa}: {quantidade}\n"

        relatorio_completo = (
            f"{relatorio_simples}\n"
            f"{produtos_estocados_por_empresa}"
        )

        return relatorio_completo
