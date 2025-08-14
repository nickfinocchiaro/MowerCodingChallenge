# Use official Python 3.13 Alpine image
FROM python:3.13-alpine

# Set work directory
WORKDIR /src

# Copy project files
COPY . /src

# install dependencies from requirements.txt
RUN pip install .

# Expose port for uvicorn
EXPOSE 8000

# start the FastAPI application using uvicorn
CMD ["uvicorn", "src.main:lawnmower_app", "--host", "0.0.0.0", "--port", "8000"]
