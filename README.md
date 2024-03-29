﻿# Kasi-Konnections

Kasi Konnections is a platform designed to address logistical challenges and inefficiencies, particularly in black communities. The focus is on improving access to essential goods and streamlining delivery services. The inspiration for this project stems from the recognition of the growing reliance on online platforms globally, with an awareness that local communities often lack these conveniences due to demographic and financial disparities.

## Usage

- **User Registration:** Users can create accounts as customers or drivers, gaining access to third-party supermarkets within the platform.
  
- **Third-Party Supermarkets:** Customers can browse products, add items to their cart, and complete the checkout process through integrated third-party supermarkets.

- **Automated Order Matching:** Upon checkout, the system automates the search for and matching of available drivers for the order.

- **Order Tracking:** Customers can track the status of their orders, including when the order is with the third-party supermarket and when it's with the driver.

- **Driver Management:** Drivers can track and manage the orders they have accepted, start and end delivery, and receive payment for their services.

## Technology Stack

- **Backend:** Flask (Python), Flask-SQLAlchemy for database management.

- **Authentication:** Flask-Login, JWT (JSON Web Tokens) for secure user authentication.

- **Database:** SQLite for development, consider migrating to a more robust solution for production.

- **Frontend:** HTML, CSS, Bootstrap for styling, and JavaScript for dynamic features.

- **Maps Integration:** Google Maps API for location-based services and routing.

## Installation

1. Clone the repository: `git clone https://github.com/nandz080/kasi-konnections.git`

2. Install dependencies: `pip install -r requirements.txt`

3. Configure database settings in `config.py`.

4. Run the application: `python app.py`


## Contributing

Contributions are welcome! Please follow the [Contribution Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the [MIT License](LICENSE).
