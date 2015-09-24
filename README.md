# PelicanReceiver
Post to a Pelican blog by email.

## Installation

Place the "/receiver" folder in your Pelican directory.

## Config

Place a `config.json` file in the `receiver` directory.
Lay out the `receiver/config.json` file as follows:

``` json
{
  "login": {
    "imap_server":"_SERVER_",
    "imap_port":993,
    "smtp_server":"_SERVER_",
    "smtp_port":465,
    "username":"_USERNAME_",
    "password":"_PASSWORD_"
  }
}
```

## Usage

Send an email to the email address provided in the config file.
The script will automatically filter the beginning of the subject line and process the content accordingly.

For a location update, the subject of the email should read:

`Location: LOCATION NAME`

For a new post, the subject of the email should read:

`Post: POST NAME HERE`

Currently, one photo can be included in a post. The photo will be placed in `content/images` and placed at the top of the blog post.

