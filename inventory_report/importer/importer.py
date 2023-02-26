from abc import ABC, abstractclassmethod
from typing import List


class Importer(ABC):
    @staticmethod
    @abstractclassmethod
    def import_data(caminho_para_o_arquivo: str) -> List[dict]:
        raise NotImplementedError
