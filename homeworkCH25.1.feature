Scenario Outline: buying
  Given John has <start> Bitcoins
  When market was down John purchased <bought> Bitcoins
  Then John should have <summary> Bitcoins


  Examples:
    |start|bought|summary|
    |2|2|4|


Feature: Multiple account users
  Only owner can change the password, except users who can only use website
  Background:
    Given an owner named John
    And access for changing password
    And user named Tom

  Scenario: John is changing password for account
    Given I am logged as John
    When I try to change account password
    Then I shoud see "You changed your password successfully"


  Scenario: Tom tries to change account password
    Given I am logged as Tom
    When I try to change account password
    Then I should see "Your attempt was failed"