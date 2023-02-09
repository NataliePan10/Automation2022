Feature: Add to cart new products
  Scenario: Adding new products through "Add to cart" button
    Given a web browser is at the Botanikabeauty home page
    When user selects new product
    And user clicks "Add to cart" button
    Then new product is added to the cart