from selene import browser, have
import os
from hw_l9.model.user import User


class RegistrationPage:
    def __init__(self):
        self.results_table = browser.element(".table-responsive")

    def open(self):
        browser.open("/automation-practice-form")
        return self

    def register(self, user: User):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._select_gender(user.gender)
        self._fill_phone_number(user.phone_number)
        self._set_birth_date(user.birth_year, user.birth_month, user.birth_day)
        self._fill_subjects(user.subjects)
        self._select_hobbies(user.hobbies)
        self._upload_picture(user.picture)
        self._fill_current_address(user.address)
        self._select_state(user.state)
        self._select_city(user.city)
        self._submit()
        return self

    def should_have_registered(self, user: User):
        browser.element("#example-modal-sizes-title-lg").should(
            have.text("Thanks for submitting the form")
        )
        self.results_table.should(have.text(f"{user.first_name} {user.last_name}"))
        self.results_table.should(have.text(user.email))
        self.results_table.should(have.text(user.gender))
        self.results_table.should(have.text(user.phone_number))
        self.results_table.should(
            have.text(f"{user.birth_day} {user.birth_month},{user.birth_year}")
        )
        self.results_table.should(have.text(user.subjects))
        self.results_table.should(have.text(user.hobbies))
        self.results_table.should(have.text(user.picture))
        self.results_table.should(have.text(user.address))
        self.results_table.should(have.text(f"{user.state} {user.city}"))

    def _fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def _fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def _fill_email(self, value):
        browser.element("#userEmail").type(value)

    def _select_gender(self, value):
        browser.all("[name=gender]").element_by(have.value(value)).element("..").click()


    def _fill_phone_number(self, value):
        browser.element("#userNumber").type(value)

    def _set_birth_date(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").click().type(year).press_enter()
        browser.element(".react-datepicker__month-select").click().type(month).press_enter()
        browser.element(f".react-datepicker__day--{int(day):03d}").click()

    def _fill_subjects(self, value):
        browser.element("#subjectsInput").type(value).press_enter()

    def _select_hobbies(self, value):
        hobbies = value.split(", ")
        for hobby in hobbies:
            browser.all("label.custom-control-label").element_by(
                have.exact_text(hobby)
            ).click()

    def _upload_picture(self, file_path):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "tests/files", file_path)
            )
        )

    def _fill_current_address(self, value):
        browser.element("#currentAddress").type(value)

    def _select_state(self, value):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()

    def _select_city(self, value):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()

    def _submit(self):
        browser.element("#submit").click()
