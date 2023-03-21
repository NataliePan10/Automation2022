Feature: Adding new products to the cart
#  Scenario: Adding new products through "Add to cart" button
#    Given Botanikabeauty home page is launched
#    When the user selects New Products from Shop Menu
#    And user clicks 'Add to cart' button
#    Then product is added to the cart
#
#
#  Scenario: Adding new products through "Quickshop" button
#    Given Botanikabeauty home page is launched
#    When the user selects New Products from Shop Menu
#    And user clicks "Quickshop" button
#    And user clicks "Add to cart" btn on popup
#    Then product is added to the cart

#
  Scenario: Adding more than one new products through "Quickshop" button by typing amount of product
    Given Botanikabeauty home page is launched
    When the user selects New Products from Shop Menu
    And user clicks "Quickshop" button
    And user types amount of new products
    And user clicks "Add to cart" btn on popup
    Then product is added to the cart
##
#
#  Scenario: Adding more than one new products through "Quickshop" button by increasing arrow
#    Given Botanikabeauty home page is launched
#    When the user selects New Products from Shop Menu
#    And user clicks "Quickshop" button
#    And user increases quantity of new products
#    And user clicks "Add to cart" btn on popup
#    Then product is added to the cart


#  Scenario: Adding more than one new products by clicking "Add to cart" button
#    Given Botanikabeauty home page is launched
#    When user selects new product
#    And user clicks "Add to cart" button as many times as needed
#    Then correct amount of new products are added to the cart