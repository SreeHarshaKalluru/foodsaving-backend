from django.test import TestCase
from foodsaving.groups.factories import GroupFactory
from foodsaving.users.factories import UserFactory
from foodsaving.groups.serializers import GroupDetailSerializer, GroupPreviewSerializer


class TestGroupSerializer(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = GroupFactory(members=[UserFactory() for _ in range(3)])

    def test_detail(self):
        serializer = GroupDetailSerializer(self.group)
        self.assertEqual(len(serializer.data.keys()), 11)
        self.assertEqual(serializer.data['id'], self.group.id)
        self.assertEqual(serializer.data['name'], self.group.name)
        self.assertEqual(serializer.data['description'], self.group.description)
        self.assertEqual(serializer.data['members'],
                         [_.id for _ in self.group.members.all()])

    def test_preview(self):
        serializer = GroupPreviewSerializer(self.group)
        self.assertEqual(len(serializer.data.keys()), 8)
        self.assertEqual(serializer.data['id'], self.group.id)
        self.assertEqual(serializer.data['name'], self.group.name)
