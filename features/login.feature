Feature: Login
  In order to have unlimited powers
  As a system anonymous user
  I want to login in the system

  Scenario Outline: Successful and unsuccessful login
    Given that there is a user registered in the system with the username "admin" and the password "123"
    When I navigate to the login page
    And fill the username field with <login>
    And fill the password field with <password>
    And click the "Log in" button
    Then I see the message <message>

  Examples:
    | login | password | message                                  |
    | admin | 123      | Welcome to admin                         |
    | admin | 1234     | Error. Verify your username and password |

