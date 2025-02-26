# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /hello_project

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir django djangorestframework djangorestframework-simplejwt

# Expose port
EXPOSE 8000

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
