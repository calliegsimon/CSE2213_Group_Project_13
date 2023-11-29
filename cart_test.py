import sqlite3
import pytest

from inventory import Inventory
from cart import cart

class TestCart_Inventory:

    @pytest.fixture

    def setup_test(self):
        test_cart = cart("Store_Database.db", "Cart")
        test_inven = Inventory("Store_Database.db", "Inventory")

        yield test_cart, test_inven

        test_cart.closeConnection()
        test_inven.close_connection()


    def test_checkOut_decreaseStock(self, capsys):
        test_inven = Inventory("anw734", "Inventory")

        test_cart = cart("Store_Database.db", "Cart")
        test_cart.addToCart("anw734", 9780307278449)
        test_cart.addToCart("anw734", 9780307278449)
        test_cart.checkOut("anw734")

        #verify
        test_inven.cursor.execute(f"SELECT Stock FROM {test_inven.table_name} WHERE ISBN = '9780307278449';")

        result = test_inven.cursor.fetchone()
        assert result[0] == 7


