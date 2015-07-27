import pytest

from django.contrib.messages.storage.fallback import FallbackStorage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.test import RequestFactory

from ..views import (
    process_items,
    delete_items,
    ViewItems,
    DELETE_COMMAND
)

from taxonomies.tests.factories import (
    TaxonomyFactory,
    TermFactory,
)

import transport


ReqFactory = RequestFactory()


def fix_messages(request):
    '''
    Save use of messages with RequestFactory.

    Stored message objects can be found in: request._messages._queued_messages
    (attributes: level, level_tag, message, tags)
    '''
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)
    return request


def check_message(request, content):
    for msg in request._messages._queued_messages:
        if msg.message == content:
            return True
    return False


@pytest.fixture
def request_item():
    '''Create item and request'''

    msg = {'body': "Message text"}
    transport.items.create(msg)

    [item] = list(transport.items.list())

    url = reverse('data-view-process')
    request = ReqFactory.post(url, {
        'action': 'batchupdate-top',
        'batchaction-top': DELETE_COMMAND,
        'select_item_id': [item['id']]}
    )
    request = fix_messages(request)

    return [request, item]


def check_item_was_deleted(request):
    assert check_message(request, u"Successfully deleted 1 item.") is True

    items = list(transport.items.list())
    assert len(list(items)) == 0


@pytest.mark.django_db
def test_delete_items_deletes_items(request_item):
    req, item = request_item
    delete_items(req, [item['id']])
    check_item_was_deleted(req)


@pytest.mark.django_db
def test_process_items_deletes_items(request_item):
    req, item = request_item
    process_items(req)
    check_item_was_deleted(req)


def test_process_items_always_redirects_to_data_view():
    url = reverse('data-view-process')
    redirect_url = reverse('data-view')

    request = ReqFactory.get(url)

    response = process_items(request)
    assert response.url == redirect_url
    assert isinstance(response, HttpResponseRedirect) is True

    request.method = 'POST'
    request = ReqFactory.post(url, {})
    request = fix_messages(request)
    response = process_items(request)
    assert response.url == redirect_url
    assert isinstance(response, HttpResponseRedirect) is True


@pytest.mark.django_db
def test_get_category_options_uses_terms():
    # TODO: Rewrite tests to use transport layer
    ebola_questions = TaxonomyFactory(name="Ebola Questions")
    other_taxonomy = TaxonomyFactory(name="Should be ignored")
    type_1 = TermFactory(
        name="Measures",
        taxonomy=ebola_questions,
        long_name="What measures could end Ebola?",
    )
    type_2 = TermFactory(
        name="Survivors",
        taxonomy=ebola_questions,
        long_name="Are survivors stigmatized?",
    )
    type_3 = TermFactory(
        name="Victims",
        taxonomy=ebola_questions,
        long_name="Number of Victims?",
    )
    other_term = TermFactory(
        name="Should be ignored",
        taxonomy=other_taxonomy,
    )

    view = ViewItems()
    options = view.get_category_options(ebola_questions.id)

    assert (type_1.name, type_1.long_name) in options
    assert (type_2.name, type_2.long_name) in options
    assert (type_3.name, type_3.long_name) in options
    assert (other_term.name, other_term.long_name) not in options


@pytest.mark.django_db
def test_get_category_options_with_no_taxonomy_returns_all():
    # TODO: Rewrite tests to use transport layer
    ebola_questions = TaxonomyFactory(name="Ebola Questions")
    other_taxonomy = TaxonomyFactory(name="Should be ignored")
    type_1 = TermFactory(
        name="Measures",
        taxonomy=ebola_questions,
        long_name="What measures could end Ebola?",
    )
    other_term = TermFactory(
        name="Some other thing",
        taxonomy=other_taxonomy,
    )

    view = ViewItems()
    options = view.get_category_options()

    assert (type_1.name, type_1.long_name) in options
    assert (other_term.name, other_term.long_name) in options


@pytest.mark.django_db
def test_get_category_options_orders_by_lowercase_name():
    # TODO: Rewrite tests to use transport layer
    ebola_questions = TaxonomyFactory(name="Ebola Questions")
    test_term_values = [
        ('test a1', '1'), ('test b1', '2'),
        ('test A2', '3'), ('test B2', '4')
    ]
    for test_value in test_term_values:
        TermFactory(
            name=test_value[0],
            long_name=test_value[1],
            taxonomy=ebola_questions
        )

    view = ViewItems()
    options = view.get_category_options(ebola_questions.id)
    # Make sure we are only comparing with out test values!
    options = [o for o in options if o in test_term_values]

    # Expected is the list ordered by lowercase short name.
    expected = sorted(test_term_values, key=lambda e: e[0].lower())

    assert options == expected


def test_views_item_get_request_parameters_renames_items_of_active_location():
    query = QueryDict(
        'action=something-bottom&item-top=top-value&item-bottom=bottom-value'
    )
    expected = {
        'action': 'something',
        'item': 'bottom-value',
        'item-top': 'top-value'
    }
    actual = ViewItems.get_request_parameters(query)
    assert actual.dict() == expected


def test_views_item_get_request_parameters_sets_default_location():
    query = QueryDict(
        'action=something&item-top=top-value&item-bottom=bottom-value'
    )
    expected = {
        'action': 'something',
        'item': 'top-value',
        'item-bottom': 'bottom-value'
    }
    actual = ViewItems.get_request_parameters(query)
    assert actual.dict() == expected


def test_views_item_get_request_parameters_sets_default_action_and_location():
    query = QueryDict(
        'item-top=top-value&item-bottom=bottom-value'
    )
    expected = {
        'action': 'none',
        'item': 'top-value',
        'item-bottom': 'bottom-value'
    }
    actual = ViewItems.get_request_parameters(query)
    assert actual.dict() == expected
