Feature: Card transaction

  @browser.chrome
  Scenario: User uses an invalid card to pay
    Given User is on the Card Form
    When User fills in an invalid card
    And User clicks Pay Now
    Then User should see a failure message

  @browser.chrome
  Scenario: User uses a valid card to pay
    Given User is on the Card Form
    When User fills in a valid card
    And User clicks Pay Now
    Then User should see the session balance has been set to unlimited
