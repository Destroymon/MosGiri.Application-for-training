from selenium.webdriver.common.by import By
from BaseApp import BasePage


class FoxLocators:
    """Локаторы."""

    TRY_BOTTOM = (By.XPATH, "//div[@id='recorddiv212347202']/div[3]/div/div/div/div/div/div[2]/div/a/table/"
                            "tbody/tr/td")

    FUNKCIONAL_BUTTOM = (By.XPATH, "//body/div[@id='allrecords']/div[@id='rec219150398']/div[1]/div[1]/"
                                   "div[2]/a[1]/div[1]/div[1]/div[3]")

    NAME_BOTTOM = (By.NAME, "Name")
    TELEPHONE_BOTTOM = (By.NAME, "tildaspec-phone-part[]")
    SUBBMIT_BOTTOM = (By.XPATH, "//button[@type='submit']")
    TEST_TEXT = (By.CSS_SELECTOR, "body.t-body:nth-child(2) div.t-records:nth-child(1) div.r.t-rec:nth-child(3) div.t-"
                                  "cover"":nth-child(1) div.t716 div.t-container div.t-width.t-width_10.t716"
                                  "__mainblock.t-align_c"
                                  "enter div.t-cover__wrapper.t-valign_middle div.t716__mainwrapper div:nth-child(2)"
                                  " form."
                                  "t-form.js-form-proccess.t-form_inputs-total_2.js-send-form-success > "
                                  "div.js-successbox."
                                  "t-form__successbox.t-text.t-text_md:nth-child(4)")

    CONF = (By.ID, "cookiesfpopupCloseButton")
    TEST_KEY = (By.CSS_SELECTOR, "body.t-body:nth-child(9) div.t-records:nth-child(1) div.r.t-rec:nth-child(3) "
                                 "div.t-cover:nth-child(1) div.t716 div.t-container div.t-width.t-width_10.t71"
                                 "6__mainblock.t-align_center div.t-cover__wrapper.t-valign_middle div.t716__ma"
                                 "inwrapper div:nth-child(2) form.t-form.js-form-proccess.t-form_inputs-total_2"
                                 ".js-send-form-success > div.js-successbox.t-form__successbox.t-text.t-text_"
                                 "md:nth-child(4)")


class Giri_request(BasePage):
    def name_input_name(self):
        self.driverwait(FoxLocators.NAME_BOTTOM).click()
        self.driverwait(FoxLocators.NAME_BOTTOM).clear()
        self.driverwait(FoxLocators.NAME_BOTTOM).send_keys("Алексей")

    def telephone_input(self):
        self.driverwait(FoxLocators.TELEPHONE_BOTTOM).click()
        self.driverwait(FoxLocators.TELEPHONE_BOTTOM).clear()
        self.driverwait(FoxLocators.TELEPHONE_BOTTOM).send_keys('9168771019')
        self.driverwait(FoxLocators.SUBBMIT_BOTTOM).click()

    def click_bottoms(self):
        self.driverwait(FoxLocators.TRY_BOTTOM).click()
        self.driverwait(FoxLocators.FUNKCIONAL_BUTTOM).click()

    def found_text(self):
        self.driverwait(FoxLocators.TEST_TEXT)

    def conf_click(self):
        self.driverwait(FoxLocators.CONF).click()

    def test_keys(self):
        text_done = self.driverwait(FoxLocators.TEST_KEY)
        return text_done.text
