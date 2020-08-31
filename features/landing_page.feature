Feature: Landing Page

    @browser.chrome
    Scenario: User go to landing page at https://www.got-it.io/solutions/excel-chat/
        Given User is on Landing Page
        Then User should see LogIn Modal Button

    @browser.chrome
    Scenario: User clicks on Log In Modal Button
        Given User is on Landing Page
        When User clicks on LogIn Modal Button
        Then User should see LogIn Modal