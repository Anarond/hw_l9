from hw_l9.registration_page import RegistrationPage
from hw_l9.model import users


def test_registration_high_level(browser_set):
    registration_page = RegistrationPage()
    student = users.student

    registration_page.open()
    registration_page.register(student)

    registration_page.should_have_registered(student)