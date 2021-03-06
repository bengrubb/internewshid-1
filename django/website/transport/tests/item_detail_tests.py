from __future__ import unicode_literals, absolute_import

from datetime import datetime
import pytest

from .. import items
from ..exceptions import TransportException


@pytest.fixture
def item():
    return items.create({'body': "Text",
                         'timestamp': "2015-08-14 00:00:00"})


@pytest.mark.django_db
def test_get_item_gets_item(item):
    item_data = items.get(item['id'])
    assert all(item_data[key] == item[key] for key in ['id', 'body'])


@pytest.mark.django_db
def test_get_item_throws_exception_for_unknown_id():
    UNKNOWN_ITEM_ID = 6  # I am not a prisoner
    with pytest.raises(TransportException) as excinfo:
        items.get(UNKNOWN_ITEM_ID)

    assert excinfo.value.message['detail'] == 'Not found.'


@pytest.mark.django_db
def test_get_item_formats_date_correctly(item):
    retrieved_item = items.get(item['id'])

    for date_field in ('timestamp', 'last_modified', 'created'):
        field = retrieved_item[date_field]
        assert isinstance(field, datetime), date_field
