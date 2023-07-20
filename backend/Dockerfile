# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container's working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application to the container's working directory
COPY hello.py .

# Expose the port on which the Flask app will run (change 5000 to the port your app uses if needed)
EXPOSE 5000

# Set the FLASK_APP environment variable to the main Flask application module
ENV FLASK_APP=hello.py

# Command to run the Flask application using the 'flask' command
CMD ["flask", "run", "--host", "0.0.0.0"]

