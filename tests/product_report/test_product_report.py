import pytest

from inventory_report.inventory.product import Product


@pytest.mark.xfail
def test_relatorio_produto():
    nome_da_empresa = "Cafes Nature"
    nome_do_produto = "Cafe"
    data_de_fabricacao = "2020-07-04"
    data_de_validade = "2023-02-09"
    numero_de_serie = "FR48"
    instrucoes_de_armazenamento = "instrucao"

    produto = Product(
        id,
        nome_da_empresa,
        nome_do_produto,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert repr(produto) == (
        f"O produto {nome_do_produto}"
        f" fabricado em {data_de_fabricacao}"
        f" por {nome_da_empresa} com validade"
        f" até {data_de_validade}"
        f" precisa ser armazenado {instrucoes_de_armazenamento}."
    )
