Feature: Add to cart more than one new products
  Scenario: Adding more than one new products through "Quickshop" button by typing amount of product
    Given a web browser is at the Botanikabeauty home page
    When user selects new product
    And user clicks "Quickshop" button
    And user types amount of new products
    And user clicks on "Add to cart" button
    Then correct amount of new products are added to the cart



  Scenario: Adding more than one new products through "Quickshop" button by selecting quantity of product
    Given a web browser is at the Botanikabeauty home page
    When user selects new product
    And user clicks "Quickshop" button
    And user clicks quantity of new products
    And user clicks on "Add to cart" button
    Then correct amount of new products are added to the cart

