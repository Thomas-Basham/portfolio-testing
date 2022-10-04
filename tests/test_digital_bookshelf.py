from time import sleep
import pytest

url = "https://digitalbookshelf.netlify.app/"
login_url = "https://digitalbookshelf.netlify.app/"


def test_home_page_values(logged_in_page):
    assert logged_in_page.locator("Your Digital Bookshelf")


def test_upload_url(logged_in_page):
    anchor = logged_in_page.locator("text=Add book outside of Google Books")
    assert anchor


def test_profile_url(logged_in_page):
    anchor = logged_in_page.locator("text=Profile")
    assert anchor.get_attribute("href") == "/profile"



@pytest.fixture
def logged_in_page(page):
    page.goto(login_url)
    page.click('button')

    page.fill('#username', 'python.testing.thomas@gmail.com')
    page.fill('#password', 'Testing123!!')
    page.locator("button[name=action]").click()
    # sleep(3)

    return page
