import subprocess
from shlex import quote


def test_ascii_command():
    input_text = "Hello, World!"  # Example input
    safe_input = quote(input_text)

    command = [
        "ascii",
        safe_input,  # Ensured safe
        "--font",
        "slant",
    ]

    result = subprocess.run(  # noqa: S603
        command,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Hello, World!" in result.stdout
    assert "____" in result.stdout
    assert result.returncode == 0
