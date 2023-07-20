# Use the official Nginx image as the base image
FROM nginx:latest

# Copy the custom Nginx configuration file to the container's Nginx configuration directory
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the port on which Nginx will listen (change 80 to the port your Nginx configuration uses if needed)
EXPOSE 80

# Start Nginx when the container is run
CMD ["nginx", "-g", "daemon off;"]

