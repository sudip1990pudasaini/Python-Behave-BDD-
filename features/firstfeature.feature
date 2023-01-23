Feature: AvenueCode Home Page

  Scenario: Landing page should be home page
    Given launch chrome browser
    When landed on main page
    Then verify that logo is present
    And nav bar is displayed
    And close browser