from __future__ import unicode_literals, absolute_import
import pytest

from data_layer.tests.factories import ItemFactory
from transport import items


@pytest.mark.django_db
def test_delete_item():
    ItemFactory()
    item = ItemFactory()
    assert len(items.list()) == 2

    items.delete(item.id)

    assert len(items.list()) == 1


@pytest.mark.django_db
def test_bulk_delete():
    ItemFactory()
    ids = [ItemFactory().id for i in range(10)]
    assert len(items.list()) == 11

    items.bulk_delete(ids)

    assert len(items.list()) == 1
