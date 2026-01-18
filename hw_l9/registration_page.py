from selene import browser, have
import os


class RegistrationPage:
    def __init__(self):
        self.results_table = browser.element(".table-responsive")

    def open(self):
        browser.open("/automation-practice-form")
        return self

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def select_gender(self, value):
        browser.element(f'label[for="gender-radio-{value}"]').click()
        return self

    def fill_phone_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def set_birth_date(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").click().type(year).press_enter()
        browser.element(".react-datepicker__month-select").click().type(month).press_enter()
        browser.element(f".react-datepicker__day--{day}").click()
        return self

    def fill_subjects(self, value):
        browser.element("#subjectsInput").click().type(value).press_enter()
        return self

    def select_hobbies(self, *hobbies):
        for hobby in hobbies:
            browser.element(f'label[for="hobbies-checkbox-{hobby}"]').click()
        return self

    def upload_picture(self, file_path):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "tests/files", file_path)
            )
        )
        return self

    def fill_current_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def select_state(self, value):
        browser.element("#state").click()
        browser.element("#react-select-3-input").type(value).press_enter()
        return self

    def select_city(self, value):
        browser.element("#city").click()
        browser.element("#react-select-4-input").type(value).press_enter()
        return self

    def submit(self):
        browser.element("#submit").click()
        return self

    def check_results(self, data):
        browser.element("#example-modal-sizes-title-lg").should(
            have.text("Thanks for submitting the form")
        )
        for key, value in data.items():
            self.results_table.element(f'//td[text()="{key}"]/following-sibling::td').should(
                have.text(value)
            )
        return self
