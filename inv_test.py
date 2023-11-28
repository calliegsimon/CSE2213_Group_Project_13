import sqlite3
import pytest
import re #regular expressions. this is specifically used to establish the patterns of output for tests. 

from inventory import Inventory

class TestInventory:

    @pytest.fixture #used in order to define a fixture
    #a fixture is a way to set up + provide a baseline for our tests. 

    def setup_test_inv(self):
        test_inv = Inventory("Store_database.db","Test_Inventory")

        yield test_inv

        test_inv.close_connection()


    def test_decreaseStock(self):
        test_inv = Inventory("Store_database.db","Test_Inventory")

        test_inv.decreaseStock('9781982115982')

        #verify
        test_inv.cursor.execute(f"SELECT Stock FROM {test_inv.table_name} WHERE ISBN = '9781982115982';")
        result = test_inv.cursor.fetchone()
        assert result[0] == 59


    def test_viewInventory(self, capsys):
        test_inv = Inventory("Store_database.db","Test_Inventory")
    
        test_inv.viewInventory()
        
        captured = capsys.readouterr().out #captures the output

        #defines a re expressiuon pattern in order to match expected output. 
        expected = re.compile(r'ISBN: 9781982115982,\s+Title: Pet Sematary: A Novel,\s+Author: Stephen King,\s+Genre: Horror,\s+Pages: 416,\s+ReleaseDate: 02/26/2019,\s+Stock: 59')

        #verify that the info is in the output
        #verifies expected output by using the predetermined pattern. 
        assert expected.search(captured) is not None
        #this uses re.search to check in the predetermined pattern is present in the output. 


    def test_searchInventory(self, capsys):
        test_inv = Inventory("Store_database.db","Test_Inventory")

        test_inv.searchInventory('Pet Sematary')

        captured = capsys.readouterr()

        expected = re.compile(r'ISBN: 9781982115982,\s+Title: Pet Sematary: A Novel,\s+Author: Stephen King,\s+Genre: Horror,\s+Pages: 416,\s+ReleaseDate: 02/26/2019,\s+Stock: 59')

        assert expected.search(captured.out) is not None

