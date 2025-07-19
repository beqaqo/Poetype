# Poetype

A typing game application built with Flask that allows users to practice their typing speed using poems.

## Features

- **Typing Speed Test**: Practice typing with beautiful poems
- **Author and Poem Selection**: Choose from various authors and their works
- **Real-time WPM Calculation**: Get instant feedback on your typing speed
- **Admin Interface**: Manage authors and poems through Flask-Admin
- **Responsive Design**: Works on desktop and mobile devices

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Poetype
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

6. **Initialize the database**
   ```bash
   flask init-db
   flask populate-db
   ```

7. **Run the application**
   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:5000`

## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black src/
isort src/
```

### Code Linting
```bash
flake8 src/
```

### Database Migrations
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Project Structure

```
Poetype/
├── app.py                 # Application entry point
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project configuration
├── env.example           # Environment variables template
├── instance/             # Instance-specific files (database, config)
├── static/               # Static files (CSS, JS, images, fonts)
├── templates/            # HTML templates
├── tests/                # Test files
└── src/                  # Application source code
    ├── __init__.py       # Application factory
    ├── config.py         # Configuration classes
    ├── ext.py            # Flask extensions
    ├── commands.py       # CLI commands
    ├── admin/            # Admin interface
    ├── models/           # Database models
    ├── utils/            # Utility functions
    └── views/            # Route handlers
```

## Configuration

The application uses environment variables for configuration:

- `SECRET_KEY`: Flask secret key for sessions
- `DATABASE_URL`: Database connection string
- `FLASK_ENV`: Environment (development/production)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.