Feature: successful login

  Scenario: Login to avenueCode test application
    Given I launch the chrome browser
    And I am on the login page
    When I enter email "sudip_pudasaini@hotmail.com" and password "assessmentqa"
    And I click on sign in button
    Then I should be logged in successfully and message is "Signed in successfully." displayed
    And I should be landed on the my tasks page
    And title of the task page should be "Hey Sudip, this is your todo list for today:"