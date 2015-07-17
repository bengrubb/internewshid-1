from __future__ import unicode_literals, absolute_import
import pytest
from rest_framework.test import APIRequestFactory
from data_layer.tests.factories import ItemFactory
from taxonomies.tests.factories import TermFactory

from ..views import ItemViewSet


def get(data=None):
    view = ItemViewSet.as_view(actions={'get': 'list'})
    request = APIRequestFactory().get('/', data)
    return view(request)


@pytest.mark.django_db
def test_get_items_returns_empty_if_no_items():
    response = get()

    assert response.data == []


@pytest.mark.django_db
def test_get_items_returns_all_items():
    item = ItemFactory(body='test')

    items = get().data

    assert len(items) == 1
    [item] = items
    assert item['body'] == 'test'


@pytest.mark.django_db
def test_filter_by_body():
    ItemFactory(body="one")
    ItemFactory(body="two")

    payload = get(data={'body': 'one'}).data

    assert len(payload) == 1
    assert payload[0]['body'] == "one"


@pytest.mark.django_db
def test_filter_by_id_list():
    ItemFactory()
    item_ids = [ItemFactory().id for i in range(10)]

    payload = get(data={'ids': item_ids}).data

    assert len(payload) == 10


@pytest.mark.django_db
def test_item_listed_with_associated_terms():
    item = ItemFactory()
    terms = [TermFactory() for i in range(3)]
    for term in terms:
        item.terms.add(term)

    [api_item] = get().data
    nested_terms = api_item['terms']

    assert len(nested_terms) == 3
    term_names = [term.name for term in terms]
    assert all(t['name'] in term_names for t in nested_terms)
