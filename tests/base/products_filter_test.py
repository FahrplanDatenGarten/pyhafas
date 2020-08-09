from pyhafas.profile.base import BaseFormatProductsFilterHelper


class ProductsFilterTestProfile(BaseFormatProductsFilterHelper):
    availableProducts = {
        'long_distance_express': [1, 2],
        'long_distance': [4],
        'regional_express': [8, 16],
    }

    defaultProducts = [
        'long_distance_express',
        'long_distance',
    ]


def test_base_products_filter_without_customization():
    products_filter = ProductsFilterTestProfile().format_products_filter({})
    assert products_filter == {
        'type': 'PROD',
        'mode': 'INC',
        'value': "7"
    }


def test_base_products_filter_with_customization():
    products_filter = ProductsFilterTestProfile().format_products_filter({
        "long_distance_express": False,
        "regional_express": True
    })
    assert products_filter == {
        'type': 'PROD',
        'mode': 'INC',
        'value': "28"
    }
