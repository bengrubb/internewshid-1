from __future__ import unicode_literals, absolute_import
import pytest

from data_layer.models import Item

from taxonomies.tests.factories import (
    TaxonomyFactory,
    TermFactory)
from transport import items
from ..exceptions import TransportException


@pytest.fixture
def item_data():
    item = {'body': "What is the cuse of ebola?"}
    return items.create(item)


@pytest.mark.django_db
def test_terms_can_be_added_to_item(item_data):
    item_id = item_data['id']
    # TODO: Replace with Term list() ?
    item = Item.objects.get(pk=item_id)
    assert item.terms.count() == 0

    for term in (TermFactory() for i in range(2)):
        items.add_term(item_id, term.taxonomy.slug, term.name)

    assert item.terms.count() == 2


@pytest.mark.django_db
def test_add_term_fails_if_term_does_not_exist(item_data):
    with pytest.raises(TransportException) as excinfo:
        items.add_term(
            item_data['id'],
            "unknown-slug",
            "unknown term name",
        )

    error = excinfo.value.message

    assert error['status_code'] == 400
    assert error['detail'] == "Term matching query does not exist."