from rest_framework import status
from rest_framework.reverse import reverse


# noinspection PyUnresolvedReferences
class MixinViewCreateTest:

    def test_create(self):
        for label, data in self.valid_data.items():
            with self.subTest(msg=label):
                response = self.client.post(
                    reverse(self.url_list),
                    data=data
                )
                self.assertEqual(
                    status.HTTP_201_CREATED,
                    response.status_code,
                    msg=repr(response.data)
                )


# noinspection PyUnresolvedReferences
class MixinViewListTest:

    def test_list(self):
        response = self.client.get(reverse(self.url_list))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            msg=repr(response.data)
        )
        data = response.data['results']
        for index, item in enumerate(data):
            with self.subTest(msg=f'List index {index}'):
                self.assertSetEqual(
                    set(self.model_factory.API_READ_FIELDS),
                    set(item.keys())
                )


# noinspection PyUnresolvedReferences
class MixinViewDeleteTest:

    def test_delete(self):
        for instance in self.instances:
            with self.subTest(msg=f'Model pk={instance.pk}'):
                response = self.client.delete(
                    reverse(self.url_detail, kwargs={'pk': instance.pk})
                )
                self.assertEqual(
                    response.status_code,
                    status.HTTP_204_NO_CONTENT,
                    msg=repr(response.data)
                )


# noinspection PyUnresolvedReferences
class MixinViewRetrieveTest:

    def test_retrieve(self):
        for instance in self.instances:
            with self.subTest(msg=f'Model pk={instance.pk}'):
                response = self.client.get(
                    reverse(self.url_detail, kwargs={'pk': instance.pk})
                )
                self.assertEqual(
                    response.status_code,
                    status.HTTP_200_OK,
                    msg=repr(response.data)
                )
                self.assertSetEqual(
                    set(self.model_factory.API_READ_FIELDS),
                    set(response.data.keys())
                )


# noinspection PyUnresolvedReferences
class MixinViewUpdateTest:

    def test_update(self):
        instance = self.instances[0]
        for label, data in self.valid_data.items():
            with self.subTest(msg=label):
                response = self.client.patch(
                    reverse(self.url_detail, kwargs={'pk': instance.pk}),
                    data=data
                )
                self.assertEqual(
                    status.HTTP_200_OK,
                    response.status_code,
                    msg=repr(response.data)
                )
                self.assertSetEqual(
                    set(self.model_factory.API_READ_FIELDS),
                    set(response.data.keys())
                )
