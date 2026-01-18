from selene import browser, have
import os


def test_form(browser_set):
    browser.open("/automation-practice-form")

    browser.element("#firstName").type("JOE")
    browser.element("#firstName").should(have.value("JOE"))

    browser.element("#lastName").type("PEACH")
    browser.element("#lastName").should(have.value("PEACH"))

    browser.element("#userEmail").type("joe@peach.com")
    browser.element("#userEmail").should(have.value("joe@peach.com"))

    browser.element("#userNumber").type("5550199045")
    browser.element("#userNumber").should(have.value("5550199045"))

    browser.element('label[for="gender-radio-1"]').click()
    browser.element("#gender-radio-1").should(have.attribute("checked"))

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").click().type("1999").press_enter()
    browser.element(".react-datepicker__month-select").click().type(
        "april"
    ).press_enter()
    browser.element(".react-datepicker__day--013").click()
    browser.element("#dateOfBirthInput").should(have.value("13 Apr 1999"))

    browser.element("#subjectsInput").click().type("ma").press_enter()
    browser.element("#subjectsContainer").should(have.text("Maths"))

    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element("#hobbies-checkbox-1").should(have.attribute("checked"))
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element("#hobbies-checkbox-2").should(have.attribute("checked"))
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element("#hobbies-checkbox-3").should(have.attribute("checked"))

    browser.element("#uploadPicture").send_keys(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "files", "png.png"))
    )

    browser.element("#currentAddress").type("3-я улица Строителей, дом 25, квартира 12")
    browser.element("#currentAddress").should(
        have.value("3-я улица Строителей, дом 25, квартира 12")
    )

    browser.element("#state").click()
    browser.element("#react-select-3-input").type("Raj").press_enter()
    # browser.element('#state').should(have.value('Rajasthan'))

    browser.element("#city").click()
    browser.element("#react-select-4-input").type("Jaise").press_enter()
    # browser.element('#state').should(have.value('Jaiselmer'))

    browser.element("#submit").click()
    browser.element("#example-modal-sizes-title-lg").should(
        have.text("Thanks for submitting the form")
    )

    browser.element('//tbody//td[text()="Student Name"]/following-sibling::td').should(
        have.text("JOE PEACH")
    )
    browser.element('//tbody//td[text()="Student Email"]/following-sibling::td').should(
        have.text("joe@peach.com")
    )
    browser.element('//tbody//td[text()="Gender"]/following-sibling::td').should(
        have.text("Male")
    )
    browser.element('//tbody//td[text()="Mobile"]/following-sibling::td').should(
        have.text("5550199045")
    )
    browser.element('//tbody//td[text()="Date of Birth"]/following-sibling::td').should(
        have.text("13 April,1999")
    )
    browser.element('//tbody//td[text()="Subjects"]/following-sibling::td').should(
        have.text("Maths")
    )
    browser.element('//tbody//td[text()="Hobbies"]/following-sibling::td').should(
        have.text("Sports, Reading, Music")
    )
    browser.element('//tbody//td[text()="Picture"]/following-sibling::td').should(
        have.text("png.png")
    )
    browser.element('//tbody//td[text()="Address"]/following-sibling::td').should(
        have.text("3-я улица Строителей, дом 25, квартира 12")
    )
    browser.element(
        '//tbody//td[text()="State and City"]/following-sibling::td'
    ).should(have.text("Rajasthan Jaiselmer"))