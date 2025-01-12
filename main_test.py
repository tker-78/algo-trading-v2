import subprocess

def test_echo():
    result = subprocess.run(['python3', 'main.py', '--echo', 'hello'],
                            capture_output=True, text=True)
    assert result.stdout.strip() == 'hello'