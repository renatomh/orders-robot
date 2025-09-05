from robocorp.tasks import task
from robocorp import browser

from RPA.HTTP import HTTP
from RPA.Tables import Tables


@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    browser.configure(
        # slowmo=1000,
    )
    orders = get_orders()
    open_robot_order_website()
    for order in orders:
        place_order(order)


def download_orders_csv():
    """Download the orders CSV file"""
    HTTP().download(
        url="https://robotsparebinindustries.com/orders.csv",
        target_file="output/orders.csv",
        overwrite=True,
    )


def get_orders() -> list[dict]:
    """Get the orders from the CSV file"""
    download_orders_csv()
    tables = Tables()
    orders = tables.read_table_from_csv("output/orders.csv")
    return orders


def open_robot_order_website():
    """Open the robot order website"""
    browser.goto("https://robotsparebinindustries.com/#/robot-order")


def close_annoying_modal():
    """Close the annoying modal"""
    page = browser.page()
    page.click("button:text('OK')")


def place_order(order: dict):
    """Place the order"""
    page = browser.page()
    close_annoying_modal()
    fill_order_form(order)
    page.click("#preview")
    page.click("#order")
    successfully_orderded = page.is_visible("#order-another")
    while not successfully_orderded:
        page.click("#order")
        successfully_orderded = page.is_visible("#order-another")
    page.click("#order-another")


def fill_order_form(order: dict):
    """Fill the order form with the order data"""
    page = browser.page()
    page.select_option("#head", str(order["Head"]))
    page.click("#id-body-" + order["Body"])
    # The leg selector should be retrieved from the placeholder text
    page.fill(
        "xpath=//input[@placeholder='Enter the part number for the legs']",
        order["Legs"],
    )
    page.fill("#address", order["Address"])
