Feature: My account access

    Scenario: A user can access to account
      Given user is on Brainbucket home page
      When user clicks "My account" button
      And user enters all needed information
      Then user has access to his account