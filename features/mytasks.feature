Feature: Create tasks

  Background: All common steps
    Given I am logged in with "sudip_pudasaini@hotmail.com" and password "assessmentqa"
    And I land on my tasks page
    And tasks input field is displayed
    And create a task button is displayed


  Scenario: Check the title
    Then title of the task page should be "Hey Sudip, this is your todo list for today:"

  Scenario Outline: Go to MyTasks page and create tasks
    When I type "<text>" in tasks input field
    And click on the add button
    Then I should see the task getting added in the list

    Examples:
      | text |
      | ABC |
      | This is my first task |
      | Tasks with 250 characters: This is the task with long characters and is about 250 char limit. Character Counter is a 100% free online character count calculator that's simple to use. Sometimes users prefer simplicity over all of the detailed writing.|
      | Tasks with 251 characters: This is the task with long characters and is about 250 char limit. Character Counter is a 100% free online character count calculator that's simple to use. Sometimes users prefer simplicity over all of the detailed writing.1|
      | Tasks with special characters: !@#$%<tag><br></br> |

  Scenario: Verify empty task is not created
    When I type "    " in tasks input field
    And click on the add button
    Then I should not see the empty task getting added

  Scenario Outline: Hard limit task char length of 250
    When I type "<text>" in tasks input field
    And click on the add button
    Then task of char length 254 should not get added

    Examples:
      | text |
      | Tasks with 254 characters: This is the task with long characters and is about 250 char limit. Character Counter is a 100% free online character count calculator that's simple to use. Sometimes users prefer simplicity over all of the detailed writing.1234|

  Scenario: Task must have minimum 3 characters
    When I type "a" in tasks input field
    And click on the add button
    Then I should not see the task getting added with less than 3 characters