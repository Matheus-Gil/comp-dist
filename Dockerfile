# Use the official Python 3.8 slim image as the base image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /comp-dist

# Copy the necessary files and directories into the container
COPY .. /comp-dist/
COPY cfg/ /comp-dist/cfg
COPY requirements.txt /comp-dist/
COPY /instance /comp-dist/instance

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the Flask application
EXPOSE 8080

CMD ["python", ".\/setup.py"]