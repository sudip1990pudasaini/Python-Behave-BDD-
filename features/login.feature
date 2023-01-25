Feature: AvenueCode test login page

  Scenario: Landing page should display navbar and email, password field and sign-in button
    Given launch chrome browser
    When landed on test login page
    Then verify that login page is displayed
    And nav bar is displayed
    And email field label is displayed
    And email input field is displayed
    And password field label is displayed
    And password input field is displayed
    And remember me checkbox is displayed
    And sign in button is displayed
    And close browser