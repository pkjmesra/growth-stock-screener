import pandas as pd
import os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from typing import Callable, List


def percent_change(initial: float, final: float) -> float:
    """Calculate the percent change between two positive numbers."""
    if initial == 0:
        raise ZeroDivisionError("Initial value of zero is undefined!")

    if pd.isna(initial) or pd.isna(final):
        raise ValueError("NaN inputs are undefined!")

    return 100 * (final - initial) / initial


def relative_strength(
    q1_start: float,
    q1_end: float,
    q2_start: float,
    q2_end: float,
    q3_start: float,
    q3_end: float,
    q4_start: float,
    q4_end: float,
) -> float:
    """Calculate the raw relative strength of a stock given its price at the starts and ends of four trading quarters."""
    q1_change = percent_change(q1_start, q1_end)
    q2_change = percent_change(q2_start, q2_end)
    q3_change = percent_change(q3_start, q3_end)
    q4_change = percent_change(q4_start, q4_end)

    return 0.2 * (q1_change) + 0.2 * (q2_change) + 0.2 * (q3_change) + 0.4 * (q4_change)


def print_status(process: str, stage: int, starting: bool) -> None:
    """Print a header or footer for each screen iteration."""
    if starting:
        print(f"\n****** Begin Stage {stage} [{process}] ******\n")
    else:
        print(f"\n****** Stage {stage} [{process}] Finished ******\n")


def skip_message(symbol: str, message: str) -> str:
    """Return a custom message logging screening errors."""
    return f"\nSkipping {symbol} ({message}) . . .\n"


def filter_message(symbol: str) -> str:
    """Return a custom message for logging when a stock is filtered out by a screen."""
    return f"\n{symbol} filtered out.\n"


def open_outfile(filename: str) -> pd.DataFrame:
    """Open json outfile data as pandas dataframe."""
    json_path = os.path.join(os.getcwd(), "backend", "json", f"{filename}.json")
    df = pd.read_json(json_path)
    return df


def create_outfile(data: pd.DataFrame, filename: str) -> None:
    """Serialize a pandas dataframe in JSON format and save in ".\\backend\\json" directory."""
    serialized_json = data.to_json()
    outfile_path = os.path.join(os.getcwd(), "backend", "json", f"{filename}.json")

    with open(outfile_path, "w") as outfile:
        outfile.write(serialized_json)


def extract_value(element: WebElement) -> float:
    """Consume a WebElement and return its value as a float."""
    try:
        return float(element.text.replace(",", "").replace(" ", ""))
    except:
        return None


def element_is_float(xpath: str) -> Callable[[WebDriver], bool]:
    """Consumes an xpath and returns a function which consumes a WebDriver and returns true if the DOM element
    at the specified xpath is a float type."""

    def inner(driver: WebDriver) -> bool:
        return type(extract_value(driver.find_element(By.XPATH, xpath))) == float

    return inner


class WaitForAll:
    """Represents an expected condition which is the logical "and" of multiple expected conditions."""

    def __init__(self, methods: List[Callable[[WebDriver], bool]]):
        self.methods = methods

    def __call__(self, driver: WebDriver) -> bool:
        try:
            for method in self.methods:
                if not method(driver):
                    return False
            return True
        except StaleElementReferenceException:
            return False
