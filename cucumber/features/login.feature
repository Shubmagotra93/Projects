Feature: Login Feature
    Scenario: Login with valid credentials
        Given open browser
        When Enter username "Admin" and password "admin123"
        Then click login button


    Scenario: Login with invalid credentials
        Given open browser
        When Enter username "Admin" and password "admin1231213"
        Then click login button
