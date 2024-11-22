# Use the jbarlow83/ocrmypdf image as the base
FROM jbarlow83/ocrmypdf:v16.6.2

# Install python3-venv package to enable virtual environment creation
RUN apt-get update && apt-get install -y python3-venv

# Create /app directory and set it as the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install Python dependencies in a virtual environment
RUN python3 -m venv /appenv && \
    /appenv/bin/pip install --no-cache-dir -r requirements.txt

# Copy application files into the container
COPY server.py index.htm entrypoint.sh /app/
COPY static /app/static/

# Ensure the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Expose the application port
EXPOSE 8000

# Set the entry point for the container, which will start the server
ENTRYPOINT ["/app/entrypoint.sh"]
