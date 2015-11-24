from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from .models import Foo
from json import loads


class IndexViewTest(TestCase):

    def test_index_view_with_no_foos(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No foos available.")
        self.assertQuerysetEqual(response.context['foo_list'], [])

    def test_index_with_one_foo(self):
        Foo.objects.create(name='Example foo',
                                         text='Lorem ipsum')
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(response.context['foo_list'],
                                 ['<Foo: Example foo>'])

    def test_index_with_several_foos(self):
        foos = [Foo.objects.create(name='Example foo %s' % number,
                                   text='Lorem ipsum')
                for number in xrange(10)]
        response = self.client.get(reverse('index'))
        self.assertEqual(len(response.context['foo_list']), len(foos))


class DetailViewTest(TestCase):

    def test_detail_view_for_existing_foo(self):
        Foo.objects.create(name='Example foo',
                           text='Lorem ipsum',)
        response = self.client.get(
            reverse('detail', args=[slugify('Example foo')])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lorem ipsum')

    def test_detail_view_for_non_existent_foo(self):
        response = self.client.get(
            reverse('detail', args=[slugify('Example foo')])
        )
        self.assertNotEqual(response.status_code, 200)


class APIViewTest(TestCase):

    def test_api_view_with_no_foos(self):
        response = self.client.get(reverse('api'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '[]')

    def test_api_view_with_several_foos(self):
        foos = [Foo.objects.create(name='Example foo %s' % number,
                                   text='Lorem ipsum')
                for number in xrange(10)]
        response = self.client.get(reverse('api'))
        self.assertEqual(response.status_code, 200)
        try:
            loaded_json = loads(response.content)
            self.assertIsInstance(loaded_json, list)
            self.assertIsInstance(loaded_json[0], dict)
            self.assertEqual(len(loaded_json), len(foos))
        except ValueError:
            self.fail('No JSON object could be decoded')

class ModelFooTest(TestCase):

    def test_as_json_contains_all_fields(self):
        fields = [field.name for field in list(Foo._meta.get_fields())]
        example_foo = Foo.objects.create(name='Example foo',
                                         text='Lorem ipsum',)
        self.assertEqual(
            set(example_foo.as_json().keys()),
            set(fields)
        )

    def test_several_foos_sharing_same_name(self):
        foos = [Foo.objects.create(name='Example foo',
                                   text='Lorem ipsum',)
                for x in xrange(10)]
        self.assertNotEqual(foos[0].slug, foos[4].slug)
        self.assertEqual(
            len(set([foo.slug for foo in foos])),
            len(foos),
        )
