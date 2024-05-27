class test_storage_data:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    Email = 'username'
    Password = 'password'
    Login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    Profile_image = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img'
    Logout_button = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
    No_user = '//form/div[text()="No User Available with this credentials"]'
    valid_email = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/div/div/p'
    Wrong_password = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[3]/span'
    No_valid_email_expected = ' Enter a valid Email'

