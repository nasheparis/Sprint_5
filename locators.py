from selenium.webdriver.common.by import By


class TestLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    SIGN_IN_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'

    # Кнопка "Зарегистрироваться" на странице входа
    SIGN_UP_BUTTON = By.XPATH, '//*[contains(@href, "register")]'

    # Ввод имени в поле "Имя" на странице регистрации
    NAME_INPUT_SIGN_UP = By.XPATH, '//*[text()="Имя"]/following-sibling::input'

    # Ввод электронной почты в поле "Email" на странице регистрации
    EMAIL_INPUT_SIGN_UP = By.XPATH, '//*[text()="Email"]/following-sibling::input'

    # Ввод пароля в поле "Пароль" на странице регистрации
    PASSWORD_INPUT_SIGN_UP = By.XPATH, '//*[text()="Пароль"]/following-sibling::input'

    # Кнопка "Зарегистрироваться" на странице регистрации
    SIGN_UP_BUTTON_TO_REGISTER = By.XPATH, '//*[contains(@class, "button_button_size_medium")]'

    # Прелоадер
    LOADING_SPINNER = By.XPATH, '//div[@class="loading-spinner"]'

    # Надпись "Некорректный пароль" на странице регистрации
    INVALID_PASSWORD = By.XPATH, '//*[contains(@class, "input__error")]'

    # Ввод электронной почты в поле "Email" на странице входа
    EMAIL_INPUT_SIGN_IN = By.XPATH, '//*[text()="Email"]/following-sibling::input'

    # Ввод пароля в поле "Пароль" на странице входа
    PASSWORD_INPUT_SIGN_IN = By.XPATH, '//*[text()="Пароль"]/following-sibling::input'

    # Кнопка "Войти" на странице входа
    SIGN_IN_BUTTON_TO_SIGN_IN = By.XPATH, '//button[contains(., "Войти")]'

    # Кнопка "Оформить заказ", которая появляется только если пользователь вошел в аккаунт
    PLACE_ORDER_BUTTON = By.XPATH, './/button[text()="Оформить заказ"]'

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//p[contains(text(), "Личный Кабинет")]'

    # Кнопка "Войти" на странице регистрации
    SIGN_IN_BUTTON_ON_SIGN_UP_PAGE = By.XPATH, '//a[@href="/login"]'

    # Кнопка "Восстановить пароль" на странице входа
    RESET_PASSWORD_BUTTON = By.XPATH, '//a[@href="/forgot-password"]'

    # Кнопка "Войти" на странице восстановления пароля
    SIGN_IN_BUTTON_ON_RESET_PASSWORD_PAGE = By.XPATH, '//a[@href="/login"]'

    # Текст на странице личного кабинета
    TEXT_IN_PERSONAL_ACCOUNT = By.XPATH, '//p[text()="В этом разделе вы можете изменить свои персональные данные"]'

    # Кнопка "Конструктор" в хедере
    CONSTRUCTOR_BUTTON = By.XPATH, ('//p[contains(@class, "AppHeader_header__linkText")][contains(text(), '
                                    '"Конструктор")]')

    # Кнопка лого сайта в хедере
    LOGO_BUTTON = By.XPATH, '//*[name()="svg"][@xmlns="http://www.w3.org/2000/svg"][@fill="none"]'

    # Кнопка "Выйти" на странице личного кабинета
    SIGN_OUT_BUTTON = By.XPATH, '//button[contains(text(),"Выход")]'

    # Раздел "Соусы"
    SAUCES_SECTION = By.XPATH, '//span[contains(@class, "text_type_main-default") and text()="Соусы"]'

    # Позиция "Соус"
    SAUCE_ITEM = By.XPATH, '//p[contains(@class, "BurgerIngredient_ingredient__text") and text()="Соус Spicy-X"]'

    # Раздел "Начинки"
    FILLINGS_SECTION = By.XPATH, '//span[contains(@class, "text_type_main-default") and text()="Начинки"]'

    # Заголовок раздела "Начинки" в каталоге
    FILLINGS_SECTION_HEADING = By.XPATH, '//h2[contains(@class, "text_type_main-medium") and text()="Начинки"]'

    # Раздел "Булки"
    BUNS_SECTION = By.XPATH, '//span[contains(@class, "text_type_main-default") and text()="Булки"]'

    # Заголовок раздела "Булки" в каталоге
    BUNS_SECTION_HEADING = By.XPATH, '//h2[contains(@class, "text_type_main-medium") and text()="Булки"]'

