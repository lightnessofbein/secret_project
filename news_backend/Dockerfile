FROM python:3.8


# Set working directory
WORKDIR /app

# Copy application code
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Expose port
EXPOSE 6543

# Start PostgreSQL and Pyramid application
CMD python app.py