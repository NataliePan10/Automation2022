Feature: New products availability

  Scenario: Show new available products
    Given a web browser is at the Botanikabeauty home page
    When the user selects New Products from Shop Menu
    Then the available new products are displayed