Feature: Card payment

  @browser.chrome
  Scenario: User chooses the card payment option
    Given User clicks on Card Option to open Card Form
    Then User should see Card Form

  @browser.chrome
  Scenario: User uses valid card information
    Given User clicks on Card Option to open Card Form
    When User fills in valid card information
    Then User should see no error message

  @browser.chrome
  Scenario: User uses incomplete card number
    Given User clicks on Card Option to open Card Form
    When User fills in incomplete card number
    Then User should see an error message

  @browser.chrome
  Scenario: User uses incomplete card date
    Given User clicks on Card Option to open Card Form
    When User fills in incomplete card date
    Then User should see an error message

  @browser.chrome
  Scenario: User uses incomplete card cvv
    Given User clicks on Card Option to open Card Form
    When User fills in incomplete card cvv
    Then User should see an error message

  @browser.chrome
  Scenario: User uses incomplete card postal
    Given User clicks on Card Option to open Card Form
    When User fills in incomplete card postal
    Then User should see an error message
