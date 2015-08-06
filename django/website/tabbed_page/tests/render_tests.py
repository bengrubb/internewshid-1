from mock import patch
import pytest

from .factories import (
    TabbedPageFactory,
    TabInstanceFactory,
)

from ..tab_pool import register_tab, BasicHtmlTab
from ..templatetags.render_tab import render_tab


class MockTabInstance(object):
    pass


render_to_string_method = 'tabbed_page.templatetags.render_tab.render_to_string'


@pytest.mark.django_db
@patch(render_to_string_method)
def test_uses_template_name(mock_render):
    tab = BasicHtmlTab()
    register_tab('basic-html-tab', tab)

    page = TabbedPageFactory()
    tab_instance = TabInstanceFactory(page=page, view_name='basic-html-tab')

    render_tab(None, tab_instance)

    args, _ = mock_render.call_args
    assert args[0] == tab.template_name


@pytest.mark.django_db
@patch(render_to_string_method)
def test_uses_context(mock_render):
    test_context = {'is_test_tab': True}

    with patch.object(BasicHtmlTab, 'get_context_data') as mock_get_context:
        mock_get_context.return_value = test_context

        tab = BasicHtmlTab()
        register_tab('basic-html-tab', tab)

        page = TabbedPageFactory()
        tab_instance = TabInstanceFactory(page=page, view_name='basic-html-tab')

        render_tab(None, tab_instance)

    _, kwargs = mock_render.call_args
    assert kwargs['context'] == test_context


@pytest.mark.django_db
@patch(render_to_string_method)
def test_uses_request(mock_render):
    tab = BasicHtmlTab()
    register_tab('basic-html-tab', tab)

    page = TabbedPageFactory()
    tab_instance = TabInstanceFactory(page=page, view_name='basic-html-tab')

    request = 'a request'
    context = {'request': request}
    render_tab(context, tab_instance)

    _, kwargs = mock_render.call_args
    assert kwargs['request'] == request


@pytest.mark.django_db
@patch(render_to_string_method)
def test_settings_passed_to_widget_get_context_data(render_to_string_method):
    with patch.object(BasicHtmlTab, 'get_context_data') as mock_get_context:
        tab = BasicHtmlTab()
        register_tab('basic-html-tab', tab)

        page = TabbedPageFactory()
        columns = ['body', 'timestamp', 'network_provider']
        settings = {'columns': columns}
        tab_instance = TabInstanceFactory(page=page,
                                          view_name='basic-html-tab',
                                          settings=settings)
        render_tab(None, tab_instance)

    _, kwargs = mock_get_context.call_args
    assert kwargs['columns'] == columns
