from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

lista_de_produtos = [
    {
        "id": 1,
        "nome_do_produto": "Cafe",
        "nome_da_empresa": "Cafes Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "instrucao"
    }
]


def test_decorar_relatorio():
    relatorio_colorido = ColoredReport(SimpleReport)

    relatorio = relatorio_colorido.generate(lista_de_produtos)

    assert '\033[32m' in relatorio
    assert '\033[36m' in relatorio
    assert '\033[31m' in relatorio
