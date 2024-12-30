import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


def selectAswers(answersSize, answeredSection):
    result = []
    currentIndex = 0
    answerIndex = 0

    for answers in answersSize:
        randomAnswerIndex = random.randint(0, answers - 1)

        absolute_index = currentIndex + randomAnswerIndex
        result.append(absolute_index)
        currentIndex += answers
        answerIndex += 1
    return result


def answerMultipleForm(numberOfForms):

    view_url = "https://docs.google.com/forms/d/e/1FAIpQLSc2MdTPmju5ZkVbI8d9ZqVWFERRcQXYRPQ2PxS6okUlkaVVeQ/viewform"
    driver = webdriver.Chrome()

    for index in range(numberOfForms):
        driver.get(view_url)
        time.sleep(2.5)
        answerForm(driver)

    driver.quit()

def answerForm(driver):

    answeredSection = 0
    while True:

        answersSize = []
        answers = driver.find_elements(By.CSS_SELECTOR, '[role="radio"]')
        submitButtons = driver.find_elements(By.XPATH, '//div[@role="button"]//span[text()="Avanti" or text()="Invia"]')

        if not answers or not submitButtons:
            return

        index = 0
        while index < len(answers):
            ariaSetsize = int(answers[index].get_attribute("aria-setsize"))
            answersSize.append(ariaSetsize)
            index += ariaSetsize

        answersIndex = selectAswers(answersSize,answeredSection)

        answerCount = 0
        for answer in answers:
            if answerCount in answersIndex:
                answer.click()
                time.sleep(0.1)
            answerCount += 1

        submitButtons[0].click()
        answeredSection +=1
        time.sleep(2)

if __name__ == "__main__":

    numberOfForms = 3
    answerMultipleForm(numberOfForms)