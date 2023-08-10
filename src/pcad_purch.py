"""
    class for purchase information
"""


class price_type:
    """class for price types
    """
    PRICE_TYPE_PCS="Price per piece"
    PRICE_TYPE_DIM="Price per dimension"

class purch:
    """mother class for purchasin
    """
    def __init__(self,link:str="", price:float=0.0, price_type=price_type.PRICE_TYPE_PCS, price_dim:float=None) -> None:
        """constructor

        Args:
            link (str, optional): link or reference to seller. Defaults to "".
            price (float, optional): price as float. Defaults to 0.0.
            price_type (_type_, optional): type of price (pieces or dimension). Defaults to price_type.PRICE_TYPE_PCS.
            price_dim (float, optional): dimension value in case the price type is for the dimension. Defaults to None.
        """
        self.set_link(link)
        self.set_price(price)
        self.set_price_type(price_type)
        self.set_price_dim(price_dim)
        pass

    def set_link(self, link:str):
        """setter for link

        Args:
            link (str): link or reference to seller
        """
        self.link = link

    def set_price(self, price:float):
        """setter for price

        Args:
            price (float): price as float
        """
        self.price=price

    def set_price_type(self, price_type:price_type):
        """ setter for price type

        Args:
            price_type (price_type): type of price (pieces or dimension)
        """
        self.price_type=price_type

    def set_price_dim(self, price_dim):
        """ setter for dimension for price calculation

        Args:
            price_dim (_type_): dimension value in case the price type is for the dimension
        """
        self.price_dim=price_dim

    def get_price(self) -> float:
        """getter for price. calulates the price in case the price type is for the dimension

        Raises:
            Exception: in case price type is for the dimension but no dimension is given

        Returns:
            float: price
        """
        if self.price_type==price_type.PRICE_TYPE_DIM:
            if self.price_dim == None:
                raise Exception ("No dimension for price calculation")
            else:
                return self.price_dim * self.price
        return self.price
