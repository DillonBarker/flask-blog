Feature: Website Homepage

    Scenario Outline: Components
        Given I load the website
        When I go to "Home" page
        Then I see this component "<article>"
        