import copy

"""
    class for purchase information
"""
import sys
sys.path.append("../")

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from tabulate import tabulate

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
    def copy(self):
        return copy.deepcopy(self)
class purch_report:
    STR_PRICE = "price"
    STR_SOURCE = "Source"
    STR_PRICE_CLASS = "price class"
    STR_PRICE_CLASS_PCS = "price/pcs"
    STR_PRICE_CLASS_DIM = "price/dim"
    STR_DIM = "dim"
    STR_PRICE_UNIT = "price per unit"
    STR_PRICE_LIST = "price list"
    STR_PRICE_SUMMARY = "Summary"

    def __init__(self, l_obj:list, filename:str) -> None:
        self.l_obj= l_obj
        self.d_purch = {self.STR_PRICE_LIST:{}, self.STR_PRICE_SUMMARY:0.0}

        for i_obj in l_obj:
            self.obj_get_price(i_obj)
        self.make_report_text()
        pass

    def make_report_text(self):
        l_tab = []
        for item in self.d_purch[self.STR_PRICE_LIST].keys():
            l_tab.append([item,
                          self.d_purch[self.STR_PRICE_LIST][item][self.STR_DIM],
                          self.d_purch[self.STR_PRICE_LIST][item][self.STR_PRICE_CLASS],
                          self.d_purch[self.STR_PRICE_LIST][item][self.STR_PRICE],
                          self.d_purch[self.STR_PRICE_LIST][item][self.STR_PRICE_UNIT],
                          self.d_purch[self.STR_PRICE_LIST][item][self.STR_SOURCE]])
        print(tabulate(l_tab, headers=["Name", "dim", "price class" "Price[€]", "Price/Unit[€]", "Source"]))
        f_sum = self.d_purch[self.STR_PRICE_SUMMARY]
        print (f"Summary: {f_sum}")
        pass

    def obj_get_price(self, i_obj):
        purch = i_obj.purch
        if purch != None and purch.price_type==price_type.PRICE_TYPE_PCS:
            f_price = i_obj.purch.get_price()
            self.d_purch[self.STR_PRICE_SUMMARY] += f_price
            self.d_purch[self.STR_PRICE_LIST][i_obj.name] = \
                {   self.STR_DIM: i_obj.purch.price_dim,
                    self.STR_PRICE_CLASS: self.STR_PRICE_CLASS_PCS,
                    self.STR_PRICE: i_obj.purch.get_price(),
                    self.STR_PRICE_UNIT: None,
                    self.STR_SOURCE: i_obj.purch.link}
        elif purch != None and purch.price_type==price_type.PRICE_TYPE_DIM:
            f_price = i_obj.purch.get_price()
            self.d_purch[self.STR_PRICE_SUMMARY] += f_price
            self.d_purch[self.STR_PRICE_LIST][i_obj.name] = \
                {   self.STR_DIM: i_obj.purch.price_dim,
                    self.STR_PRICE_CLASS: self.STR_PRICE_CLASS_DIM,
                    self.STR_PRICE: i_obj.purch.get_price(),
                    self.STR_PRICE_UNIT: i_obj.purch.price,
                    self.STR_SOURCE: i_obj.purch.link}
        elif purch == None:
            #self.d_purch[self.STR_PRICE_LIST][i_obj.name] = {self.STR_PRICE: None, self.STR_PRICE_UNIT: None, self.STR_SOURCE:None}
            pass
        else:
            raise Exception ("Unknown constallation")

    def cube(self, i_obj):
        self.obj_get_price(i_obj)

    def cylinder(self, i_obj):
        self.obj_get_price(i_obj)

    def aobj(self, i_obj):
        self.obj_get_price(i_obj)

    def dim(self, i_obj):
        pass

    def sobj(self, i_obj):
        self.obj_get_price(i_obj)

