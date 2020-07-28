import abc


class FormatProductsFilterHelperInterface(abc.ABC):
    @abc.abstractmethod
    def format_products_filter(self, requested_products: dict) -> dict:
        """
        Create the products filter given to HaFAS

        :param requested_products: Mapping of Products to whether it's enabled or disabled
        :return: value for HaFAS "jnyFltrL" attribute
        """
        pass
