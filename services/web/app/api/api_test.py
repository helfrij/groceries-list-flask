from unittest import TestCase
from unittest.mock import patch, call
from webtest import TestApp
from app import create_app
from app.config import TestConfig
from app.domain import GroceryList


class BaseUnitTest(TestCase):
    def setUp(self) -> None:
        self.app = TestApp(create_app(TestConfig))


class TestGetGroceryLists(BaseUnitTest):
    @patch('app.api.api.repository')
    def test_get_grocery_lists_returns_empty_list(self, mock_repository):
        grocery_lists = []
        mock_repository.get_grocery_lists.return_value = grocery_lists

        response = self.app.get('/grocery_lists')
        assert response.status_int == 200
        assert isinstance(response.json, dict)
        assert response.json['data'] == []

        mock_repository.get_grocery_lists.assert_has_calls([call()])

    @patch('app.api.api.repository')
    def test_get_grocery_lists_returns_grocery_list(self, mock_repository):
        grocery_lists = [GroceryList(1, 'Groceries', [])]
        mock_repository.get_grocery_lists.return_value = grocery_lists

        response = self.app.get('/grocery_lists')
        assert response.status_int == 200
        assert isinstance(response.json, dict)
        assert response.json['data'] == [{'id': 1, 'name': 'Groceries', 'items': []}]

        mock_repository.get_grocery_lists.assert_has_calls([call()])
