### List of things to do:

1. Build the Docker image using the Dockerfile.
2. Run the Docker container, exposing port 5000 on the host.
3. Verify that the application is running correctly by testing the /ping endpoint.
4. Add a health check that calls the /ping endpoint.
5. Create a custom Docker network.
6. Stop the current container and re-run it, connecting it to the custom network.
7. Write a bash script that will return me a wholesome llama meme when the /meme_me endpoint is called.