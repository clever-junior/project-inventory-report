import pytest

from inventory_report.inventory.product import Product


@pytest.mark.xfail
def test_cria_produto():
    product = Product(
        id,
        nome_do_produto="",
        nome_da_empresa="",
        data_de_fabricacao="",
        data_de_validade="",
        numero_de_serie="",
        instrucoes_de_armazenamento="",
    )

    assert repr(product)
