from datetime import datetime 

def format_date(date_str):
    dt = datetime.strptime(date_str , "%Y-%m-%d %H:%M:%S")
    return dt.strftime("%b %d, %Y %I:%M %p")

""" 
| Format | Example Output      |
| ------ | ------------------- |
| `%b`   | `Jan`, `Feb`, `May` |
| `%d`   | `01`, `25`, `31`    |
| `%Y`   | `2023`, `2025`      |
| `%I`   | `01`, `12`          |
| `%M`   | `00`, `45`          |
| `%p`   | `AM`, `PM`          |
"""

def validate_amount(input_str):
    try: 
        return float(input_str)
    except ValueError :
        return None