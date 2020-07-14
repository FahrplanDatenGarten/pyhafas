import abc


class FormatProductsFilterHelperInterface(abc.ABC):
    @abc.abstractmethod
    def format_products_filter(self, requested_products: dict) -> dict:
        pass
