Feature: Payment modal

  @browser.chrome
  Scenario: User can see the payment modal
    Given User is already logged in and clicks on Subscription Button to open payment modal
    Then User should see payment modal
    And User should see card payment option
    And User should see Paypal payment option

