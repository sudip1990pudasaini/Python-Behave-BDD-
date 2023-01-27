Feature: Manage subtasks

  Background: All common steps
    Given I am logged in with "sudip_pudasaini@hotmail.com" and password "assessmentqa"
    And I land on my tasks page
    When a task is added

  Scenario: Manage subtasks button
    Then I should see manage subtasks button
    And subtasks counter should be zero

  Scenario: Click manage subtasks button opens up subtasks modal
    When I click on manage subtasks button
    Then it should open up the subtasks modal
    And modal has the edit subtask title

  Scenario: Task description is read-only
    When I click on manage subtasks button
    Then task description should be read-only
    # TODO [1104 Task description under manage sub-tasks modal is not read only]
    #  this should get passed when reported bug is fixed and remove this comment

  Scenario: Subtask description is required
    When I click on manage subtasks button
    And I click on add subtask button
    Then I should not see an empty subtask getting added
    # TODO [1105 Sub-task description and Due date should be required]
    #  this should get passed when reported bug is fixed and add check for validation message

  Scenario: Subtask due date is required
    When I click on manage subtasks button
    And I wipe out the default date value
    And I click on add subtask button
    Then I should not see an empty subtask getting added
    # TODO [1105 Sub-task description and Due date should be required]
    #  this should get passed when reported bug is fixed and add check for validation message


  Scenario Outline: Due date accepts only date value on MM/dd/yyy
    When I click on manage subtasks button
    And I wipe out the default date value
    And enter "<value>" on due date field
    And I click on add subtask button
    Then I should not see an empty subtask getting added

    Examples:
    |  value |
    |    asd fads f |
    |  @#$!@#!@#!@#  |
    | 123123123123 |
    # TODO [1106 Due Date field takes any value]
    #  this should get passed when reported bug is fixed and add check for validation message

  Scenario Outline: Add subtask and see counter is increased
    When I click on manage subtasks button
    And enter text "<subtask_text>" on subtask description
    And I click on add subtask button
    Then I should see the subtask getting added

    When I close the modal
    Then I subtask counter "<count>" on manage subtask button should be increased


    Examples:
    | count |  subtask_text |
    | 1 | This is the first sub-task |
    | 2 | This is the sub-task with special chars: @#$@#123  |
    | 3 | Sub-tasks with 250 chars: This is the task with long characters and is about 250 char limit. Character Counter is a 100% free online character count calculator that's simple to use. Sometimes users prefer simplicity over all of the detailed writing.|
