#Excersise 1

  Scenario Outline: buying
  Given John has <start> Bitcoins
  When John purchases <amount> Bitcoins
  Then John should have <summary> Bitcoins


  Examples:
    |start|amount|summary|
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
    Then I should see "You changed your password successfully"


  Scenario: Tom tries to change account password
    Given I am logged as Tom
    When I try to change account password
    Then I should see "Your attempt was failed"


#Exersise 3

  Feature: Show Wishlist

    Scenario: Show items in wishlist
      Given a web browser is at Brainbucket home page account
      When the user navigates to wishlist
      Then wishlist items are displayed


  Feature: Products

    Scenario: A user can add product to the cart
      Given user is on Brainbucket homepage
      When user clicks "Add to cart" button
      Then user sees product in the cart





  Feature: My account

    Scenario: A user can access to account
      Given user is on Brainbucket home page
      When user clicks "My account" button
      And user enters all needed information
      Then user has access to his account
