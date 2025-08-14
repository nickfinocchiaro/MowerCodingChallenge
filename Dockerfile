# Use official Python 3.13 Alpine image
FROM python:3.13-alpine

# Set work directory
WORKDIR /src

# Install build dependencies for pip (for packages with wheels)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy project files
COPY . /src

# Create and activate virtual environment
RUN python -m venv /venv
ENV VIRTUAL_ENV=/venv
ENV PATH="/venv/bin:$PATH"

# install dependencies from requirements.txt
RUN pip install .

# Expose port for uvicorn
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "src.main:lawnmower_app", "--host", "0.0.0.0", "--port", "8000"]
