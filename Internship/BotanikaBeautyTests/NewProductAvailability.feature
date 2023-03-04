Feature: New products availability

  Scenario: Show new available products
    Given Botanikabeauty home page is launched
    When the user selects New Products from Shop Menu
    Then the available new products are displayed