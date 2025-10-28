from abc import ABC, abstractmethod

class BaseReport(ABC):
    @abstractmethod
    def generate(self, data):
        """Генерирует отчёт на основе списка словарей."""
        pass
