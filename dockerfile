# Use official Python image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /hello_project

# Install dependencies
COPY Pipfile Pipfile.lock /hello_project/
RUN pip install pipenv && pipenv install --system

# Copy project files
COPY . /hello_project/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
