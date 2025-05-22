def import_cookies_from_file():
    path = 'Infoga/assets/cookies.txt'
    cookies = {}
    try:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    cookies[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error reading cookies: {e}")
    return cookies


def export_cookie_by_key(cookies, key, export_path='exported_cookie.txt'):
    if key in cookies:
        try:
            with open(export_path, 'w') as file:
                file.write(f"{key}={cookies[key]}\n")
            print(f"Cookie exported to {export_path}")
        except Exception as e:
            print(f"Error writing cookie: {e}")
    else:
        print(f"Key '{key}' not found in cookies.")


def export_cookie_as_form_data(cookies, key, export_path='cookie_form_data.txt'):
    if key in cookies:
        try:
            # Escape special characters if needed here (optional)
            with open(export_path, 'w') as file:
                file.write(f"{key}={cookies[key]}")
            print(f"Cookie exported as form data to {export_path}")
        except Exception as e:
            print(f"Error exporting cookie form data: {e}")
    else:
        print(f"Key '{key}' not found in cookies.")

  key = getenv("key", 'Koushal')
