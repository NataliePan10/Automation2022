Feature: Add to cart more than one new products
  Scenario: Adding more than one new products by clicking "Add to cart" button
    Given a web browser is at the Botanikabeauty home page
    When user selects new product
    And user clicks "Add to cart" button as many times as needed
    Then correct amount of new products are added to the cart


