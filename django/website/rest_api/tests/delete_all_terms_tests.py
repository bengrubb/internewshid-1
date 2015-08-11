from __future__ import unicode_literals, absolute_import

import pytest

from django.core.urlresolvers import reverse
from rest_framework.test import APIRequestFactory
from rest_framework import status
from data_layer.models import Item
from .item_create_view_tests import create_item
from .taxonomy_and_term_create_tests import (
    create_category,
    add_term,
)
from .categorize_items_tests import (
    categorize_item,
    category,
    item,
    term
)
from ..views import ItemViewSet


def remove_categories_from_item(item, taxonomy):
    url = reverse('item-delete-all-terms', kwargs={"pk": item['id']})
    request = APIRequestFactory().post(url, {'taxonomy': taxonomy})
    view = ItemViewSet.as_view(actions={'post': 'delete_all_terms'})
    return view(request, item_pk=item['id'])


@pytest.mark.django_db
def test_all_item_categories_can_be_deleted(item, term):
    categorize_item(item, term)

    # TODO: use the API for this
    [item_orm] = Item.objects.all()
    terms = item_orm.terms.all()
    assert len(terms) == 1

    response = remove_categories_from_item(item, term['taxonomy'])
    assert status.is_success(response.status_code), response.data

    terms = item_orm.terms.all()
    assert len(terms) == 0
