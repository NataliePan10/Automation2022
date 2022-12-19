  Feature: Show Wishlist

    Scenario: Show items in wishlist
      Given a web browser is at Brainbucket home page account
      When the user navigates to wishlist
      Then wishlist items are displayed
