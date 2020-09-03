Feature: Payment modal

  @browser.chrome
  Scenario: User can see the payment modal
    Given User is logged in and clicks on Subscription Button
    Then User should see payment modal
    And User should see card payment option
    And User should see Paypal payment option

