Feature: Login99
  Scenario Outline: Login_Guru
    Given Launch Firefox browser
    Then Open Guru99 Url
    Then enter "<userid>" and "<password>"
    And click submit

    Examples:
    | userid      | password  |
    | mngr287661  | ygYguqu   |
    | mngr287661  | hghjj     |
    | hjfyjg      | kjhk      |
    | mngr287661  | ygYguqu   |



