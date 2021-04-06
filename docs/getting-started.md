# Getting started

In order to communicate with us in a secure manner, you will need to send us your GPG public key. Have a look at the Github guide to [Generating a new GPG key](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-gpg-key) if you are having difficulties.

If you are new to OAuth or Auth0, we highly recommend that you [sign up for free with Auth0](https://auth0.com/signup) and start familiarising yourself with what they have to offer and the terminology used. Once you have an Auth0 tenant up and running, make sure you read [What is the OAuth 2.0 Authorization Code Grant Type?](https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type) as this is what most clients will use.

## Clients

A client can either be a customer facing application, such as an mobile app or a web service, or a machine-to-machine client. A customer facing application should use [Authorization Code Flow](https://auth0.com/docs/flows/call-your-api-using-the-authorization-code-flow) (and preferably with [Proof Key for Code Exchange (PKCE)](https://auth0.com/docs/flows/call-your-api-using-the-authorization-code-flow-with-pkce)). 


## Requesting a new client
You can request a new client from the individual at Coop who sent you this resource. 

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

Once we have this information, along with your public key, we will create a client for you to integrate with Coop. You will recieve an encrypted bundle from us with all the technical details needed to get up and running.

Should you have specific requirements for session lifetime, absolute lifetime and the like, please let us know when requesting a client.

## You have a client, now what?

Great stuff! There are a number of tutorials out there to get you started, Auth0 has even made a series of [quick start guides](https://auth0.com/docs/quickstarts) tailored to the various applications types and programming languages. 

## Useful resources
* [Generating a new GPG key](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-gpg-key)
* [What is the OAuth 2.0 Authorization Code Grant Type?](https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type)
* [Auth0 Quickstarts](https://auth0.com/docs/quickstarts)
* [Authorization Code Flow with Proof Key for Code Exchange (PKCE)](https://auth0.com/docs/flows/call-your-api-using-the-authorization-code-flow-with-pkce). 
