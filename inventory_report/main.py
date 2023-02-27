import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    try:
        _method, file_path, report_type = sys.argv
        importer = get_importer(file_path)
        return sys.stdout.write(
            InventoryRefactor(importer).import_data(file_path, report_type))
    except ValueError:
        return sys.stderr.write("Verifique os argumentos\n")


def get_importer(caminho_para_o_arquivo: str):
    extensao_do_arquivo = caminho_para_o_arquivo.rsplit(".", 1)[-1]

    match extensao_do_arquivo:
        case "csv":
            return CsvImporter
        case "json":
            return JsonImporter
        case "xml":
            return XmlImporter


if __name__ == "__main__":
    main()
