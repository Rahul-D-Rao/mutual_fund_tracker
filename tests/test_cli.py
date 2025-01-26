import os
import sys
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

# Add specific subdirectories to sys.path
sys.path.append(os.path.abspath(os.path.join(current_dir, '../src', 'cli')))

from cli_helpers import validate_date_format

def test_validate_date_format():
    valid_date = "2025-01-01"
    invalid_date = "01-01-2025"

    assert validate_date_format(valid_date) is True
    assert validate_date_format(invalid_date) is False
