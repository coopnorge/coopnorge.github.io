# Getting started

In order to communicate with us in a secure manner, you will need to send us your GPG public key. Have a look at the Github guide to [Generating a new GPG key](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-gpg-key) if you are having difficulties with this.

## Requesting a new client
In order to configure a new client, the following info has to be provided by the client for each of the environments (development, test, staging, production) you require:

* Name - Name of your system or application from which the client will be used
* Description - Briefly describe what this client is used for
* Type of application (one of)
  * Native
  * Single Page Web app
  * Regular Web app
  * Machine to Machine
* Grant types
  * authorization_code
  * refresh_token
  * Other (Please specify which, and why)
* Callback urls
* Logout urls
* Scopes (optional)
* Audience (optional)

Once we have this information, along with your public key, we will create a client for you to integrate with Coop. 
