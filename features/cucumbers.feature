Feature: Scenario outlines
    Scenario Outline: Outlined given, when, then
        Given there are <start> cucumbers
        When I eat <eat> cucumbers
        Then I should have <left> cucumbers

        Examples:
        | start | eat | left |
        |  12   |  5  |  7   |
