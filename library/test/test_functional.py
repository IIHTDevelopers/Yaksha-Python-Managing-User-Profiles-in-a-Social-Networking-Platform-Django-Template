from django.urls import reverse
from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from library.models import UserProfile
from library.models import UserProfileForm
from django.db import models

class UserProfileFunctionalTest(TestCase):

    def test_create_user_profile(self):
        """Test if a user profile is created successfully"""
        test_obj = TestUtils()
        try:
            profile = UserProfile.objects.create(
                bio='Tech enthusiast',
                contact_info='user@example.com'
            )
            if profile:
                test_obj.yakshaAssert("TestCreateUserProfile", True, "functional")
                print("TestCreateUserProfile = Passed")
            else:
                test_obj.yakshaAssert("TestCreateUserProfile", False, "functional")
                print("TestCreateUserProfile = Failed")
        except:
            test_obj.yakshaAssert("TestCreateUserProfile", False, "functional")
            print("TestCreateUserProfile = Failed")

    def test_model_inherits_from_django_model(self):
        """Test if the model correctly inherits from Django Model"""
        test_obj = TestUtils()
        is_subclass = issubclass(UserProfile, models.Model)
        
        try:
            UserProfile.bio
        except:
            test_obj.yakshaAssert("TestModelInheritsFromDjangoModel", False, "functional")
            print("TestModelInheritsFromDjangoModel = Failed")
            return
        
        if is_subclass:
            test_obj.yakshaAssert("TestModelInheritsFromDjangoModel", True, "functional")
            print("TestModelInheritsFromDjangoModel = Passed")
        else:
            test_obj.yakshaAssert("TestModelInheritsFromDjangoModel", False, "functional")
            print("TestModelInheritsFromDjangoModel = Failed")

    def test_user_profile_form_valid(self):
        """Test if the UserProfileForm is valid when given correct data"""
        test_obj = TestUtils()
        try:
            form_data = {'bio': 'Software Engineer', 'contact_info': 'contact@example.com'}
            form = UserProfileForm(data=form_data)
            if form.is_valid():
                test_obj.yakshaAssert("TestUserProfileFormValid", True, "functional")
                print("TestUserProfileFormValid = Passed")
            else:
                test_obj.yakshaAssert("TestUserProfileFormValid", False, "functional")
                print("TestUserProfileFormValid = Failed")
        except:
            test_obj.yakshaAssert("TestUserProfileFormValid", False, "functional")
            print("TestUserProfileFormValid = Failed")
