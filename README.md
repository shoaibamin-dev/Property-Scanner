# Property Scanner App

The Property Scanner App is a versatile tool designed for scraping data from various real estate online platforms. It provides individual scrapers for different real estate apps, allowing users to execute scans on-demand. The project utilizes multiprocessing to enhance performance and expedite the scraping process.

## Project Structure

The project is organized into logical sections:

### 1. Home Directory

- **DB**: Contains database-related scripts.
  - `conn.py`: Database connection script.

- **aurorabeachfront**: Scraper module for Aurora Beachfront.
  - `aurorabeachfront.py`: Scraper script.
  - `data.json`: Sample data file.

- **emeraldinvestmentnica**: Scraper module for Emerald Investment Nica.
  - `emeraldinvestmentnica.py`: Scraper script.
  - `data.json`: Sample data file.

- **investnicaragua**: Scraper module for Invest Nicaragua.
  - `investnicaragua.py`: Scraper script.
  - `data.json`: Sample data file.

- **nicaliferealty**: Scraper module for Nicalife Realty.
  - `nicaliferealty.py`: Scraper script.
  - `data.json`: Sample data file.

- **property-nicaragua**: Scraper module for Property Nicaragua.
  - `property-nicaragua.py`: Scraper script.
  - `data.json`: Sample data file.

- **trinityrealestatenicaragua**: Scraper module for Trinity Real Estate Nicaragua.
  - `trinityrealestatenicaragua.py`: Scraper script.
  - `__pycache__`: Cached Python files.
  - `data.json`: Sample data file.
  - `db.py`: Database-related script.
  - `hmongo.py`: MongoDB connection script.
  - `hemail.py`: Email-related script.
  - `test.py`: Test script.

- **README.md**: Project documentation.

### 2. Property Data Directory

- **aurorabeachfront**: Directory for storing data from Aurora Beachfront.
  - `data.json`: Data file.

- **emeraldinvestmentnica**: Directory for storing data from Emerald Investment Nica.
  - `data.json`: Data file.

- **investnicaragua**: Directory for storing data from Invest Nicaragua.
  - `data.json`: Data file.

- **nicaliferealty**: Directory for storing data from Nicalife Realty.
  - `data.json`: Data file.

- **property-nicaragua**: Directory for storing data from Property Nicaragua.
  - `data.json`: Data file.

- **trinityrealestatenicaragua**: Directory for storing data from Trinity Real Estate Nicaragua.
  - `data.json`: Data file.

## Usage

1. **Adding New Scrapers**:
   - To add a new scraper for a real estate platform, create a new module in the home directory.

2. **Configuring Scrapers**:
   - Customize each scraper script according to the structure and data of the respective real estate app.

3. **Executing Scans**:
   - Utilize the multiprocessing capabilities to execute scans concurrently for faster results.

4. **Storing Data**:
   - Store the scraped data in the corresponding directories within the "property_data" folder.

5. **Database Integration**:
   - Modify and utilize the database scripts in the "DB" directory for data storage if required.

## Contributing

Contributions are welcome! If you have improvements or new features to suggest, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the license terms.

## Acknowledgments

Thank you for using the Property Scanner App. Your contributions and feedback are highly valued. For any queries or issues, please contact the project maintainers.

Happy scanning! 🏡✨