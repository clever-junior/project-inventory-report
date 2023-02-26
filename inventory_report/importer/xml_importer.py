import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(caminho_para_o_arquivo):
        if not caminho_para_o_arquivo.endswith("xml"):
            raise ValueError("Arquivo inválido")

        with open(caminho_para_o_arquivo, "r", encoding="utf-8") as file:
            dados_do_xml = file.read()
            return xmltodict.parse(
                dados_do_xml
            )["dataset"]["record"]
