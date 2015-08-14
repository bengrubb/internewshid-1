from django.utils.dateparse import parse_datetime
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_api.views import ItemViewSet

from .exceptions import TransportException

request_factory = APIRequestFactory()


def get_view(actions):
    return ItemViewSet.as_view(actions=actions)


def _parse_date_fields(item):
    date_fields = ('created', 'timestamp', 'last_modified', )
    item_dict = dict(item)
    for date_field in date_fields:
        value = item_dict[date_field]
        if value is not None:
            item_dict[date_field] = parse_datetime(value)
    return item_dict


def list(**kwargs):
    """ Return a list of Items

    If keyword arguments are given, they are used
    to filter the Items.
    """
    # FIXME: currently only body exact filtering is supported
    view = get_view({'get': 'list'})
    request = request_factory.get("", kwargs)

    items = view(request).data

    for item in items:
        item.update(_parse_date_fields(item))

    return items


def get(id):
    """ Return a single item specified by its id """
    view = ItemViewSet.as_view(actions={'get': 'retrieve'})
    request = request_factory.get("")
    response = view(request, pk=id)
    if status.is_success(response.status_code):
        item = response.data
        item.update(_parse_date_fields(item))

        return item
    else:
        response.data['status_code'] = response.status_code
        raise TransportException(response.data)


def create(item):
    """ Create an Item from the given dict """
    view = get_view({'post': 'create'})
    request = request_factory.post("", item)
    response = view(request)
    if status.is_success(response.status_code):
        return response.data
    else:
        response.data['status_code'] = response.status_code
        raise TransportException(response.data)


def update(id, item):
    """ Update an Item from the given dict """
    view = get_view({'put': 'update'})
    request = request_factory.put("", item)
    response = view(request, pk=id)
    if status.is_success(response.status_code):
        return response.data
    else:
        response.data['status_code'] = response.status_code
        raise TransportException(response.data)


def delete(id):
    """ Delete the Item with the given ID """
    view = get_view({'delete': 'destroy'})
    request = request_factory.delete("")
    return view(request, pk=id)


def bulk_delete(ids):
    """ Delete all Items whose ids appear in the given list """
    # DELETE http requests appear not to send query parameters so
    # for the moment I'm mapping this onto multiple calls to delete()
    for id in ids:
        delete(id)


def add_term(item_id, taxonomy_slug, name):
    """ Add term named `name` within the Taxonomy with `taxonomy_slug` to the
    Item with id `item_id`

    args:
        item_id: e.g. 67
        taxonomy_slug: e.g. 'ebola-questions'
        name: name of a Term in the Taxonomy with given slug

    returns:
        response from the server

    raises:
       TransportException on failure

    For the moment both the taxonomy and term must already exist.
    """
    view = get_view({'post': 'add_term'})

    term = {'taxonomy': taxonomy_slug, 'name': name}
    request = request_factory.post("", term)
    response = view(request, item_pk=item_id)

    if status.is_success(response.status_code):
        return response.data
    else:
        response.data['status_code'] = response.status_code
        response.data['term'] = term
        response.data['item_id'] = item_id
        raise TransportException(response.data)


def delete_all_terms(item_id, taxonomy_slug):
    view = get_view({'post': 'delete_all_terms'})

    taxonomy = {'taxonomy': taxonomy_slug}
    request = request_factory.post("", taxonomy)
    response = view(request, item_pk=item_id)

    if not status.is_success(response.status_code):
        response.data['status_code'] = response.status_code
        raise TransportException(response.data)

    return response.data
