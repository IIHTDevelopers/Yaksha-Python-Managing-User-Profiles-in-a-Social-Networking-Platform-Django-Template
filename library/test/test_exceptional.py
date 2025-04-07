
from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from library.models import UserProfile
from library.models import UserProfileForm
from django.core.files.uploadedfile import SimpleUploadedFile



class UserProfileExceptionalTest(TestCase):

    def test_invalid_profile_picture_format(self):
        """Test if an invalid profile picture format is rejected"""
        test_obj = TestUtils()
        try:
            invalid_file = SimpleUploadedFile("test.txt", b"Invalid content", content_type="text/plain")
            form_data = {'bio': 'Photographer', 'contact_info': 'contact@example.com'}
            form = UserProfileForm(data=form_data, files={'profile_picture': invalid_file})
            if not form.is_valid():
                test_obj.yakshaAssert("TestInvalidProfilePictureFormat", True, "exceptional")
                print("TestInvalidProfilePictureFormat = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidProfilePictureFormat", False, "exceptional")
                print("TestInvalidProfilePictureFormat = Failed")
        except:
            test_obj.yakshaAssert("TestInvalidProfilePictureFormat", False, "exceptional")
            print("TestInvalidProfilePictureFormat = Failed")

    def test_missing_contact_info(self):
        """Test if missing contact info results in form validation error"""
        test_obj = TestUtils()
        try:
            form_data = {'bio': 'Artist'}
            form = UserProfileForm(data=form_data)
            if not form.is_valid():
                test_obj.yakshaAssert("TestMissingContactInfo", True, "exceptional")
                print("TestMissingContactInfo = Passed")
            else:
                test_obj.yakshaAssert("TestMissingContactInfo", False, "exceptional")
                print("TestMissingContactInfo = Failed")
        except:
            test_obj.yakshaAssert("TestMissingContactInfo", False, "exceptional")
            print("TestMissingContactInfo = Failed")

    def test_max_length_bio_exceeded(self):
        """Test if bio exceeding max length raises a validation error"""
        test_obj = TestUtils()
        try:
            long_bio = "x" * 350
            form_data = {'bio': long_bio, 'contact_info': 'user@example.com'}
            form = UserProfileForm(data=form_data)
            if not form.is_valid():
                test_obj.yakshaAssert("TestMaxLengthBioExceeded", True, "exceptional")
                print("TestMaxLengthBioExceeded = Passed")
            else:
                test_obj.yakshaAssert("TestMaxLengthBioExceeded", False, "exceptional")
                print("TestMaxLengthBioExceeded = Failed")
        except:
            test_obj.yakshaAssert("TestMaxLengthBioExceeded", False, "exceptional")
            print("TestMaxLengthBioExceeded = Failed")
