import datetime

from nhour.tests.factories import UserFactory
from nhour.models import CompletedWeek
from django.contrib.auth.models import User
from django.test import TestCase, Client


class TestRoutes(TestCase):
    def setUp(self):
        self.c = Client()

    # def test_user_is_sent_to_login_page_when_accessing_main_page(self):
    #     def access_page_and_check_if_in_login(url):
    #         root = self.c.get(url, follow=True)
    #         #self.assertTrue(root.request.url.startswith("/login?next="))
    #         self.assertEqual(root.request.status, "200")
    #
    #     access_page_and_check_if_in_login('/')
    #     access_page_and_check_if_in_login('/edit/2009/09/4')

    def test_if_user_has_just_registered_they_are_sent_to_latest_weeks_registration_page(
            self):
        user = UserFactory()
        root = self._open_index(user)
        now = datetime.datetime.today()
        current_week = now.isocalendar()[1]
        self.assertEqual(root.context['week'], current_week)

    def test_if_user_has_not_completed_any_weeks_they_are_sent_to_registration_weeks_page(
            self):
        user = UserFactory()
        user.date_joined = datetime.datetime(2015, 10, 10)
        user.save()
        root = self._open_index(user)
        self.assertEqual(int(root.context['year']), 2015)
        self.assertEqual(int(root.context['week']), 41)

    def test_if_user_has_completed_weeks_they_are_sent_to_oldest_uncompleted_week(
            self):
        user = UserFactory()
        date_joined = datetime.datetime(2015, 10, 10)
        user.date_joined = date_joined
        user.save()

        CompletedWeek.objects.create(year=2015, week=43, user=user)

        root = self._open_index(user)
        self.assertEqual(int(root.context['year']), 2015)
        self.assertEqual(int(root.context['week']), 41)

        CompletedWeek.objects.create(year=2015, week=41, user=user)
        root = self._open_index(user)
        self.assertEqual(int(root.context['year']), 2015)
        self.assertEqual(int(root.context['week']), 42)

        CompletedWeek.objects.create(year=2015, week=42, user=user)
        root = self._open_index(user)
        self.assertEqual(int(root.context['year']), 2015)
        self.assertEqual(int(root.context['week']), 44)

    def _open_index(self, user):
        self.c.force_login(user)
        root = self.c.get('/')
        return root
