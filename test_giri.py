from LOCATORS import Giri_request


class Test_giri:
    """Проверка оформления заявки на Функциональную тренировку."""

    def test_untitled_test_case(self, browser):
        autorization = Giri_request(browser)
        autorization.go_to_site()
        autorization.conf_click()
        autorization.click_bottoms()
        autorization.name_input_name()
        autorization.telephone_input()
        assert autorization.test_keys() == "Спасибо! Скоро с Вами свяжется наш тренер Алексей"
