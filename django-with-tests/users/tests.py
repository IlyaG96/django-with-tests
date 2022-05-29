from django.test import TestCase
from django.contrib.auth.models import User
from .models import Owner, Dog


class UserCreationTestCase(TestCase):

    def test_user(self):
        username = 'ivan'
        password = 'ivan888'
        user = User(username=username)
        user.set_password(password)
        user.save()
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_owner_creation(self):
        owner_name = 'John'
        owner, created = Owner.objects.get_or_create(
            name=owner_name
        )
        self.assertEqual(owner.name, owner_name)
        self.assertTrue(created)

    def test_owner_with_dog_creation(self):
        owner_name = 'John'
        dog_name = 'dog_one'
        dog_breed = 'sample_breed'

        owner, created = Owner.objects.get_or_create(
            name=owner_name
        )
        dog, created = Dog.objects.get_or_create(
            name=dog_name,
            breed=dog_breed
        )
        owner.dog = dog
        owner.save()
        self.assertEqual(owner.dog.name, dog_name)
        self.assertEqual(owner.name, owner_name)
        self.assertTrue(created)




