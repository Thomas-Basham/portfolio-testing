from time import sleep
import pytest

url = "https://collab-done.vercel.app/"
login_url = "https://collab-done.vercel.app/login"


def test_home_page_values(logged_in_page):
    assert logged_in_page.inner_text("a") == "COLLAB DONE"


def test_upload_url(logged_in_page):
    anchor = logged_in_page.locator("text=Upload")
    assert anchor.get_attribute("href") == "/upload-song"


def test_profile_url(logged_in_page):
    anchor = logged_in_page.locator("text=Profile")
    assert anchor.get_attribute("href") == "/profile"



@pytest.fixture
def logged_in_page(page):
    page.goto(login_url)

    page.fill('#email', 'python.testing.thomas@gmail.com')
    page.fill('#password', 'testing')
    page.locator(".button").click()
    # sleep(3)

    return page
