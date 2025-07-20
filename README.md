# Sauce Demo Web Scraping Automation

This project automates the retrieval of inventory data from the [Sauce Demo](https://www.saucedemo.com/) website using Selenium.

## Features

- **Automated Login:** Uses credentials from environment variables for secure authentication.
- **CAPTCHA Handling:** Detects CAPTCHA and prompts for manual resolution if present.
- **Data Extraction:** Scrapes item names and descriptions from the inventory page.
- **Robust Error Handling:** Handles login errors, asynchronous loading, and missing elements gracefully.
- **Data Storage:** Saves the retrieved data to `data_retrieved.csv` in a tabular format.

## Setup

1. **Install Dependencies:**
   - Python 3.x
   - `selenium`
   - `python-dotenv`
   - `pandas`
2. **Download ChromeDriver:**  
   Download the appropriate ChromeDriver for your system and update the path in `solution.py`.
3. **Create a `.env` File:**  
   Add your Sauce Demo credentials:
   ```
   SAUCEDemo_USERNAME=your_username
   SAUCEDemo_PASSWORD=your_password
   ```
4. **Run the Script:**
   ```
   python solution.py
   ```

## How It Works

- The script loads credentials from `.env`.
- It launches Chrome, logs in, and checks for CAPTCHA.
- If CAPTCHA is detected, you are prompted to solve it manually.
- After successful login, it scrapes inventory items and descriptions.
- The data is saved to `data_retrieved.csv`.

## Notes

- If login fails, an error message is displayed.
- Manual intervention is required if CAPTCHA appears.
- The script ensures the browser is closed after execution.

## License

This project is for educational and personal use.