import requests
from requests.exceptions import RequestException


def generate_random_fact(output_format: str, language: str) -> str:
    """
    Args:
        output_format:  aaa
        language: aaaaaa

    Returns:
        eeee
    """
    # foo
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    # bar
    if response.status_code == 200:
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact
