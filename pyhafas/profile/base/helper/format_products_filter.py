from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.format_products_filter import \
    FormatProductsFilterHelperInterface
from pyhafas.types.exceptions import ProductNotAvailableError


class BaseFormatProductsFilterHelper(FormatProductsFilterHelperInterface):
    def format_products_filter(
            self: ProfileInterface,
            requested_products: dict) -> dict:
        """
        Create the products filter given to HaFAS

        :param requested_products: Mapping of Products to whether it's enabled or disabled
        :return:
        """
        products = self.defaultProducts
        for requested_product in requested_products:
            if requested_products[requested_product]:
                try:
                    products.index(requested_product)
                except ValueError:
                    products.append(requested_product)

            elif not requested_products[requested_product]:
                try:
                    products.pop(products.index(requested_product))
                except ValueError:
                    pass
        bitmask_sum = 0
        for product in products:
            try:
                for product_bitmask in self.availableProducts[product]:
                    bitmask_sum += product_bitmask
            except KeyError:
                raise ProductNotAvailableError(
                    'The product "{}" is not available in chosen profile.'.format(product))
        return {
            'type': 'PROD',
            'mode': 'INC',
            'value': str(bitmask_sum)
        }
