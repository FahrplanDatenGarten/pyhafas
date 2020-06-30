class ProductNotAvailableError(Exception):
    """Requested Product is not available in profile"""
    pass


class GeneralHafasError(Exception):
    """HaFAS returned an general error"""
    pass
