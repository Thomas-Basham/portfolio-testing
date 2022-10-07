import pytest

url = "https://thomasbashamportfolio.net/"


def test_home_page_values(page):
    page.goto(url)

    assert page.locator("text=PROJECTS")


def test_projects_loaded(page):
    page.goto(url)

    assert len(page.query_selector_all(".project-title-settings")) > 7


def test_logged_in_url(logged_in_page):
    assert logged_in_page.locator("text=Thanks for logging in,")


@pytest.fixture
def logged_in_page(page):
    page.goto(url)
    page.locator("text=Log In to Comment").click()
    page.fill('#username', 'python.testing.thomas@gmail.com')
    page.fill('#password', 'Testing123!!')
    page.locator("button[name=action]").click()

    return page
