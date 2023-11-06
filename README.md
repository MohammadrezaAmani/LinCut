# Lincut - FastAPI Link Shortener

Lincut is a simple yet powerful Link Shortener service built with FastAPI. It allows you to shorten long URLs into concise, user-friendly links.

## Features

- Shorten long URLs with ease.
- Generate customizable and memorable short links.
- View statistics on the usage of your links.
- API for easy integration with other applications.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/lincut.git

```
2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Configure your database settings and other options in the `config.py` file.

4. Start the FastAPI application:

```bash
python -m lincut
```

Lincut will be available at [http://localhost:8000](http://localhost:8000).

### Usage
Access the Lincut web interface at  [http://localhost:8000](http://localhost:8000) or your deployed server.
Enter the long URL you want to shorten.
Optionally, customize the short link or leave it to be auto-generated.
Click the "Shorten" button to generate the short link.
You can also view statistics for each short link on the dashboard.
API Documentation
Lincut provides a simple and easy-to-use API for link shortening and statistics retrieval. The API documentation can be found at http://localhost:8000/docs, powered by Swagger UI. This documentation provides details on all available API endpoints and request/response formats.

### Configuration
The config.py file allows you to configure various aspects of the Lincut service, including database settings, custom short link patterns, and more. Be sure to review and update this file to suit your specific requirements.

### Contributing
We welcome contributions to Lincut! If you would like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure the code is well-documented.
4. Run tests to make sure your changes haven't broken existing functionality.
5. Submit a pull request with a clear description of the changes and the problem they solve.
### License
Lincut is open-source software released under the `MIT` License. You are free to use, modify, and distribute it as you see fit.

If you have any questions, feedback, or issues to report, please don't hesitate to open an issue on this GitHub repository.