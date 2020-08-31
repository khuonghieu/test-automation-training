Feature: Choose pricing options

  @browser.chrome
  Scenario: User can see the storefront
    Given User is already logged in and on Pricing page
    Then User should see pricing button
    And User should see Individual and Small Business Button
    And User should see Subscription Button