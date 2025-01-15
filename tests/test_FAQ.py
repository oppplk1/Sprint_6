import pytest
import allure
from pages.home_page import HomePage
from helpers.test_data import HomePageFAQ
from helpers.locators import HomePageLocator


@allure.epic('Main page / ui usability')
@allure.parent_suite('Домашняя страница')
@allure.suite('FAQ')
class TestFAQPage:
    @allure.feature('Аккордеон с вопрос/ответ на Домашней страницы')
    @allure.story('Нажатие на вопрос в разделе "Вопросы о важном" раскрывается ответ.')
    @allure.title('Нажатие на вопрос, раскрывается ответ ')
    @allure.description('Проверка вопрос и текст')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, HomePageFAQ.answer1),
            (1, 1, HomePageFAQ.answer2),
            (2, 2, HomePageFAQ.answer3),
            (3, 3, HomePageFAQ.answer4),
            (4, 4, HomePageFAQ.answer5),
            (5, 5, HomePageFAQ.answer6),
            (6, 6, HomePageFAQ.answer7),
            (7, 7, HomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        ya_scooter_home_page = HomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_faq_question(question_number=question)
        answer = ya_scooter_home_page.find_element(HomePageLocator.FAQ_ANSWER(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer
