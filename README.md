# Dracula-Line-A-Minute
A twitter bot tweeting out Bram Stoker's 'Dracula', one tweet every minute.

https://twitter.com/LinaMinute

## Development
Built by following the tutorial at realpython.com:

https://realpython.com/twitter-bot-python-tweepy/


## Build and Run

### Building the docker image
`docker build . -t dracula-line-a-minute`

### Running docker container
`docker run -it --env-file env.list dracula-line-a-minute`


## Export image for deploy

### Exporting the docker image
`docker image save dracula-line-a-minute:latest -o dracula-line-a-minute.tar`

#### Windows:
`tar -cvzf dracula-line-a-minute.tar.gz dracula-line-a-minute.tar`

#### Mac/Linux:
`gzip dracula-line-a-minute.tar`
