import sqlite3
import pytest

from inventory import Inventory
from cart import cart

class TestCart_Inventory:

    @pytest.fixture
    def setup_test(self):
        db_name = "Store_Database.db"
        test_cart_table = "Test_Cart"
        test_inv_table = "Test_Inventory"
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        yield cart(db_name, test_cart_table), Inventory(db_name,test_inv_table)

        cursor.close()
        connection.close()


    def test_checkOut_decreaseStock(self, setup_test):
        cart, inventory = setup_test

        cart.addToCart


