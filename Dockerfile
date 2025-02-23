# Dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=open_companies_database.settings_docker

# Set work directory
WORKDIR /code

# Install dependencies
COPY pyproject.toml /code/
COPY poetry.lock /code/
RUN pip install poetry
RUN poetry install --without dev --no-root

# Copy project files
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

# Start the Django development server on port 8000
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
