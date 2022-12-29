Feature: Login functionality
  Background:
    Given User launched login page


  Scenario: a user can login using correct email and password
    Given User is not logged in
    When user enters email and password
    And user clicks Login button
    Then The user's profile page will be launched


  Scenario: User can not login without entering correct email and password
    Given User is  not logged in
    When User enters incorrect email and password
    And User clicks Login button
    Then Warning will be shown about 'No match for E-Mail Address and/or Password'