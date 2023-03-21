


Scenario Outline: buying tablets
  Given user has <start> tablet
  When user purchased <bought> tablet
  Then user should have <summary> tablets


  Examples:
    |start|bought|summary|
    |1|1|2|


Feature: Multiple account users
  Only owner can change the password, except users who can only use website
  Background:
    Given an owner named "John"
    And access for changing password
    And user named "Tom"

  Scenario: John is changing password for account on Brainbucket
    Given I am logged as John
    When I try to change account password
    Then I should see "You changed your password successfully"


  Scenario: Tom tries to change account password Brainbucket
    Given I am logged as Tom
    When I try to change account password
    Then I should see "Your attempt was failed"