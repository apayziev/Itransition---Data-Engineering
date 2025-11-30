import math
from flask import Flask, request, Response


class Config:
    """Application configuration."""
    EMAIL_SLUG = "abdulkhay_payziev_gmail_com"


app = Flask(__name__)


def validate_non_negative_integer(value: str) -> int:
    """Parse and validate a non-negative integer string."""
    if not value or not value.isdigit():
        raise ValueError(f"Invalid input: {value}")
    return int(value)


def calculate_lcm(a: int, b: int) -> int:
    """Calculate the Lowest Common Multiple of two integers."""
    return math.lcm(a, b)


@app.route(f'/{Config.EMAIL_SLUG}', methods=['GET'])
def lcm_endpoint():
    """
    GET /<email_slug>?x=<int>&y=<int>
    Returns: LCM as plain text, or "NaN" for invalid inputs.
    """
    try:
        x = validate_non_negative_integer(request.args.get('x'))
        y = validate_non_negative_integer(request.args.get('y'))
        return Response(str(calculate_lcm(x, y)), mimetype='text/plain')
    except (ValueError, TypeError):
        return Response("NaN", mimetype='text/plain')


if __name__ == '__main__':
    print(f"Server: http://127.0.0.1:5000/{Config.EMAIL_SLUG}")
    app.run(debug=True, port=5000)
    print(f"Starting server at: http://127.0.0.1:5000/{Config.EMAIL_SLUG}")
    app.run(debug=True, port=5000)