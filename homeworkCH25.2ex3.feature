  Feature: Adding products

    Scenario: A user can add product to the cart
      Given user is on Brainbucket homepage
      When user clicks "Add to cart" button
      Then user sees product in the cart