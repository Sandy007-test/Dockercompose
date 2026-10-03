FROM nginx:alpine

# Remove the default Nginx welcome configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom nginx.conf into the container
COPY nginx.conf /etc/nginx/conf.d/
