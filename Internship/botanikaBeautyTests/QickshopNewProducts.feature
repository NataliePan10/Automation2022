Feature: Quickshop new products

  Scenario: Adding new products through quickshop
    Given a web browser is at the Botanikabeauty home page
    When user selects new product
    And user clicks quickshop button
    And user clicks "Add to cart" button
    Then new product is added to the cart