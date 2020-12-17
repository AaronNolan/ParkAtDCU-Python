from django.test import TestCase
from django.urls import reverse
from .models import Campus, Carpark


class SetUpTest(TestCase):

    def test_welcome(self):
        """
      The index page loads and an appropriate welcome message is displayed
      """
        response = self.client.get(reverse('parkatdcu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to ParkAtDCU")


# class A1Tests(TestCase):
#
#     def setup(self):
#         """
#         Sets up a test database
#         """
#         campus1 = Campus(1,'Test Campus')
#         campus2 = Campus(2,'Another Test Campus')
#         campus3 = Campus(3,'Yet Another Test Campus')
#         carpark1 = Carpark(1, 'test c1',1,750,30)
#         carpark2 = Carpark(2, 'test c2',1,250,15)
#         carpark3 = Carpark(3, 'test c3',1,300,15)
#         carpark4 = Carpark(4, 'test c4',3,200,10)
#         campus1.save()
#         campus2.save()
#         campus3.save()
#         carpark1.save()
#         carpark2.save()
#         carpark3.save()
#         carpark4.save()
#
#     def setupempty(self):
#         """
#         Sets up a test database with no carparks
#         """
#         campus1 = Campus(1,'Test Campus')
#         campus2 = Campus(2,'Another Test Campus')
#         campus3 = Campus(3,'Yet Another Test Campus')
#         campus1.save()
#         campus2.save()
#         campus3.save()
#
#
#     def test_carpark_names(self):
#         """
#         Test retrieval of carpark names for a campus
#         """
#         self.setup()
#         response = self.client.get(reverse('parkatdcu:index'))
#         self.assertEqual(response.status_code,200)
#         self.assertContains(response,'c1')
#         self.assertContains(response,'c2')
#         self.assertContains(response,'c3')
#         self.assertContains(response,'c4')
#
#     def test_carpark_campusnames(self):
#         """
#         Test retrieval of campus names
#         """
#         self.setup()
#         response = self.client.get(reverse('parkatdcu:index'))
#         self.assertEqual(response.status_code,200)
#         self.assertContains(response,'Test Campus')
#         self.assertContains(response,'Yet Another Test Campus')
#
#     def test_carpark_spaces(self):
#         """
#         Test retrieval spaces
#         """
#         self.setup()
#         response = self.client.get(reverse('parkatdcu:index'))
#         self.assertEqual(response.status_code,200)
#         self.assertContains(response,'750 spaces')
#         self.assertContains(response,'30 spaces for people with disabilities')
#
#     def test_carpark_empty_retrieval(self):
#         """ Test empty retrieval of carparks """
#         self.setupempty()
#         response = self.client.get(reverse('parkatdcu:index'))
#         self.assertEqual(response.status_code,200)
#         self.assertContains(response,'No carparks found')
#
#     def test_carpark_empty_parttwo(self):
#         """ Test empty retrieval of carparks for a campus """
#         self.setup()
#         response = self.client.get(reverse('parkatdcu:index'))
#         self.assertEqual(response.status_code,200)
#         self.assertContains(response,'Another Test Campus')
#         self.assertContains(response,'No carparks found')

class A3Tests(TestCase):

    def setup(self):
        """
        Sets up a test database
        """
        campus1 = Campus(1, 'Test Campus')
        campus2 = Campus(2, 'Another Test Campus')
        campus3 = Campus(3, 'Yet Another Test Campus')
        carpark1 = Carpark(1, 'test c1', 1, 750, 30)
        carpark2 = Carpark(2, 'test c2', 1, 250, 15)
        carpark3 = Carpark(3, 'test c3', 1, 300, 15)
        carpark4 = Carpark(4, 'test c4', 3, 200, 10)
        campus1.save()
        campus2.save()
        campus3.save()
        carpark1.save()
        carpark2.save()
        carpark3.save()
        carpark4.save()

    def test_retrieval(self):
        """
        Test retrieval of carparks for a campus
        """
        self.setup()
        response = self.client.get(reverse('parkatdcu:carparks'), {'campus': 'Test Campus'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test c1')
        self.assertContains(response, 'test c2')
        self.assertContains(response, 'test c3')

    def test_empty_retrieval(self):
        """ Test empty retrieval of carparks for a campus """
        self.setup()
        response = self.client.get(reverse('parkatdcu:carparks'), {'campus': 'Another Test Campus'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No carparks found')

    def test_retrieval_invalid(self):
        """ Test retrieval of carparks for an invalid campus """
        self.setup()
        response = self.client.get(reverse('parkatdcu:carparks'), {'campus': 'invalid campus'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No such campus')

    def test_retrieval_case(self):
        """ Test retrieval of carparks for a campus (case-insensitive) """
        self.setup()
        response = self.client.get(reverse('parkatdcu:carparks'), {'campus': 'test campus'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test c1')
        self.assertContains(response, 'test c2')
        self.assertContains(response, 'test c3')
