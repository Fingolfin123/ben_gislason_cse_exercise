import unittest
from ben_gislason_cse_exercise.utilities.db_read import dbRead
from ben_gislason_cse_exercise.utilities.db_Write import dbWrite

import logging

logging.basicConfig(level=logging.DEBUG)


class dbTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        """Instantiates a dataframe from SQLite database"""
        self.df = dbRead(r"ben_gislason_cse_exercise/tests/test.db")
        print(self.df)

    def test_writeDB(self):
        """

        """
        self.df = dbRead(r"ben_gislason_cse_exercise/tests/test.db",")
    def test_transpose(self):
        """

        """
        
