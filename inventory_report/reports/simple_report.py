from datetime import date
from typing import List


class SimpleReport:
    @staticmethod
    def generate(dados_dos_produtos: List[dict]) -> str:
        datas_de_fabricacao: List[date] = []
        datas_de_validade: List[date] = []
        empresas: List[str] = []

        for produto in dados_dos_produtos:
            datas_de_fabricacao.append(
                date.fromisoformat(produto["data_de_fabricacao"])
            )

            datas_de_validade.append(
                date.fromisoformat(produto["data_de_validade"])
            )

            empresas.append(
                produto["nome_da_empresa"]
            )

        fabricacao_mais_antiga = min(datas_de_fabricacao)
        validade_mais_proxima = min(datas_de_validade)
        empresas_com_mais_produtos = max(
            set(empresas), key=empresas.count
        )

        relatorio_simples = (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {empresas_com_mais_produtos}"
        )

        return relatorio_simples
