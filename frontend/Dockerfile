# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory in the container to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the app's dependencies in the container
RUN npm install

# Copy the rest of the app's files (excluding node_modules) to the container
COPY . .

# Specify that the container should run the "npm start" command by default
CMD [ "npm", "start" ]
