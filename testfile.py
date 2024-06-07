import time
import pytest
from Actionable.actionable import Actions
import dataDrivenTesing

class TstExecutor:

    def test_login(self):
        Actions().test_gmail()


tc = TstExecutor()
tc.test_login()