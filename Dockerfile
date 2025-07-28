# Base Image
FROM python:3.9

# set working directory
WORKDIR /app

# copy all the files from the current folder to container
COPY . .

# install all the dependencies and after installation delete all the downloaded files
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the fast API
EXPOSE 8000

# Command to start fast API
CMD  ["uvicorn", "main:app","--host","0.0.0.0","--port","8000"]