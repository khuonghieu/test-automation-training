Feature: Login

  @browser.chrome
  Scenario: Successful login attempt with correct username and password
    Given User is on Login Modal
    When User fills in valid username and password
    Then User should see the account button on the navbar

  @browser.chrome
  Scenario: Fail login attempt with wrong username and password
    Given User is on Login Modal
    When User fills in invalid username and password
    Then User should see log in error message