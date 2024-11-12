### List of things to do:

1. Build the Docker image using the Dockerfile.
2. Run the Docker container, exposing port 5000 on the host.
3. Verify that the application is running correctly by testing the /ping endpoint.
4. Add a health check that calls the /ping endpoint.
5. Create a custom Docker network.
6. Stop the current container and re-run it, connecting it to the custom network.
7. Add a endpoint count_meme which returns the number of memes that exist on the server as a JSON object.
8. Write a bash script that will return me a wholesome llama meme when the `/meme_me_sh` endpoint is called.  This is currently working using at the `meme_me` endpoint but is python based.
9. Keep a in memory database of each meme that is viewed and how many times it is viewed.  Allow me to see the stats of each meme as a JSON object by calling `meme_stats`