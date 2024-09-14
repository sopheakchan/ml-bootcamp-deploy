# Use Python 3.12 slim image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the random forest model file
COPY random_forest_model.pkl /app/

# Copy the application files
COPY app.py /app/
COPY flower/ /app/flower/
COPY templates/home.html /app/templates/


# Command to run the Flask app, making sure it binds to all available IPs
CMD ["python", "app.py"]
