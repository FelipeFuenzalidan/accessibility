Feature: Google

  Scenario: Google Search
    Given I am on google search page
    When  I inject axe-core javascript into page
    And I run axe accessibility checks
    Then I write results to file