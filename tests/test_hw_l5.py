from hw_l9.registration_page import RegistrationPage


def test_registration_mid_level(browser_set):
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name("JOE")
    registration_page.fill_last_name("PEACH")
    registration_page.fill_email("joe@peach.com")
    registration_page.select_gender("1")
    registration_page.fill_phone_number("5550199045")
    registration_page.set_birth_date("1999", "april", "013")
    registration_page.fill_subjects("ma")
    registration_page.select_hobbies("1", "2", "3")
    registration_page.upload_picture("png.png")
    registration_page.fill_current_address("3-я улица Строителей, дом 25, квартира 12")
    registration_page.select_state("Raj")
    registration_page.select_city("Jaise")
    registration_page.submit()

    registration_page.check_results(
        {
            "Student Name": "JOE PEACH",
            "Student Email": "joe@peach.com",
            "Gender": "Male",
            "Mobile": "5550199045",
            "Date of Birth": "13 April,1999",
            "Subjects": "Maths",
            "Hobbies": "Sports, Reading, Music",
            "Picture": "png.png",
            "Address": "3-я улица Строителей, дом 25, квартира 12",
            "State and City": "Rajasthan Jaiselmer",
        }
    )
