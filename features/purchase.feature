Feature: Card transaction

  @browser.chrome
  Scenario: User uses an invalid card to pay
    Given User is on landing page
    And User logs in
    And User goes to pricing page
    And User chooses subscription option
    And User opens all available payment options
    And User chooses card payment option
    Then User should see Card Form
    When User fills in an invalid card
    And User clicks Pay Now
    Then User should see a failure message

  @browser.chrome
  Scenario: User fills valid card information
    Given User is on landing page
    And User logs in
    And User goes to pricing page
    And User chooses subscription option
    And User opens all available payment options
    And User chooses card payment option
    Then User should see Card Form
    When User fills in a valid card
    Then User should see no error message

  @browser.chrome
  Scenario: User uses incomplete card number
    Given User is on landing page
    And User logs in
    And User goes to pricing page
    And User chooses subscription option
    And User opens all available payment options
    And User chooses card payment option
    Then User should see Card Form
    When User fills in incomplete card number
    Then User should see card info error message

  @browser.chrome
  Scenario: User uses incomplete card date
    Given User is on landing page
    And User logs in
    And User goes to pricing page
    And User chooses subscription option
    And User opens all available payment options
    And User chooses card payment option
    Then User should see Card Form
    When User fills in incomplete card date
    Then User should see card info error message

  @browser.chrome
  Scenario: User uses incomplete card cvv
    Given User is on landing page
    And User logs in
    And User goes to pricing page
    And User chooses subscription option
    And User opens all available payment options
    And User chooses card payment option
    Then User should see Card Form
    When User fills in incomplete card cvv
    Then User should see card info error message

  @browser.chrome
  Scenario: User uses incomplete card postal
    Given User is on landing page
    And User logs in
    And User goes to pricing page
    And User chooses subscription option
    And User opens all available payment options
    And User chooses card payment option
    Then User should see Card Form
    When User fills in incomplete card postal
    Then User should see card info error message

  @browser.chrome
  @terminate_subscription
  Scenario: User uses valid card to pay
    Given User is on landing page
    And User logs in
    And User goes to pricing page
    And User chooses subscription option
    And User opens all available payment options
    And User chooses card payment option
    Then User should see Card Form
    When User fills in a valid card
    And User clicks Pay Now
    Then User should see Transaction Success Modal