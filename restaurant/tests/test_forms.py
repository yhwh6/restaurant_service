from restaurant.forms import CookCreationForm

from django.contrib.auth import get_user_model

from django.test import TestCase

from django.urls import reverse


class CookFormTest(TestCase):
    def test_cook_creation_form_with_years_of_experience_valid(self):
        form_data = {
            "username": "user",
            "password1": "user12345",
            "password2": "user12345",
            "years_of_experience": 10,
            "first_name": "First name",
            "last_name": "Last name",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_creation_form_with_years_of_experience_invalid(self):
        form_data = {
            "username": "user",
            "password1": "user12345",
            "password2": "user12345",
            "years_of_experience": "10",
            "first_name": "First name",
            "last_name": "Last name",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertNotEqual(form.cleaned_data, form_data)


class CookUpdateTest(TestCase):
    def test_cook_update_form_valid(self):
        new_cook = get_user_model().objects.create_user(
            username="user",
            password="user12345",
            years_of_experience=10,
            first_name="First name",
            last_name="Last name",
        )
        self.client.force_login(new_cook)
        update_data = {
            "years_of_experience": 10,
            "first_name": "First name",
            "last_name": "Last name",
        }

        self.client.post(
            reverse("restaurant:cook-update", kwargs={"pk": new_cook.id}),
            data=update_data,
        )

        cook = get_user_model().objects.get(pk=new_cook.id)
        self.assertEqual(
            cook.years_of_experience, update_data["years_of_experience"]
        )
        self.assertEqual(cook.first_name, update_data["first_name"])
        self.assertEqual(cook.last_name, update_data["last_name"])
