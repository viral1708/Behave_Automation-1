Feature: Verify functionality of Registration

  Scenario: Registration with valid data
    Given User is on registration page
    When User enters username
    And User enters email ID
    And User enters Password
    And User click on sign-up button
    Then User should register successfully


  Scenario: Registration with duplicate username
    Given User is on registration page
    When User enters duplicate username
    And User enters email ID
    And User enters Password
    And User click on sign-up button
    Then User should register successfully
