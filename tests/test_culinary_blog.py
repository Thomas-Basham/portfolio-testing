from time import sleep
import pytest

home_url = "https://smells-like-devs-cooking-frontend-rho.vercel.app/"
login_url = "https://smells-like-devs-cooking-frontend-rho.vercel.app/loginpage"


def test_home(page):
    page.goto(home_url)

    assert page.title() == "Smells Like Devs Cooking"
    assert page.inner_text("a") == "\xa0\xa0Home"


def test_home_page_values(logged_in_page):
    assert logged_in_page.inner_text("a") == "\xa0\xa0Home"


def test_home_page_navigation(logged_in_page):
    anchor = logged_in_page.locator("text=Create a Blog Post")
    url = anchor.get_attribute("href")
    assert url == "/create"


@pytest.fixture
def logged_in_page(page):
    page.goto(login_url)

    page.fill('#username', 'admin')
    page.fill('#password', 'admin')
    page.click('button')
    # sleep(3)

    return page
