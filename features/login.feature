Feature: AvenueCode test login page

  Scenario: Landing page should display navbar and email, password field and sign-in button
    When login page is displayed
    Then verify nav bar is displayed
    And verify email field label is displayed
    And verify email input field is displayed
    And verify password field label is displayed
    And verify password input field is displayed
    And verify remember me checkbox is displayed
    And verify sign in button is displayed