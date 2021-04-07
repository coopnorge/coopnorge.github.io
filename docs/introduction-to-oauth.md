# Introduction to OAuth 2

We use OAuth to ensure secure and convenient authentication of our users, and are relying on Auth0 as our provider.

If you are new to OAuth or Auth0, we highly recommend that you [sign up for free with Auth0](https://auth0.com/signup) and start familiarising yourself with what they have to offer and the terminology used. 

## Introduction

OAuth 2 is an authorzation framework that allows an application limited access to a user account, without the application requiring access to the users credentials (username or password). This saves the application developer from having to create mechanisms for secure storage of usernames and passwords, session expiration and more. Think of it as authentication as a service.

A core principle in OAuth is that the user (Resource Owner) is the one who authenticates and who grants access to the application (Client). The autentication is performed between the user the user database (Authorization Server), which in this case is Auth0. 

* A user is called Resource Owner
* An application is called Client
* The user database is called Authorzation Server

In order for the Client to be allowed access to the user database, it needs to be registered with the Authorization Server and issued its own and unique Client ID and Client Secret (think of it as a username and password for the client). The Client ID and Client Secret does not allow the Client to access the entire user database, but rather gives the application permission to ask the user to grant the application access to their data. 

NB: Client ID and Client Secret should be kept secure and not committed to your version control system

Although OAuth 2 allows for a few different ways of authentication a user, we will only allow using Authorization Code. 

## Tokens
There are three types of tokens issued by the authorization server

* Access token
* Refresh token
* ID token

### Access token
Access tokens are the users credentials once authenticated. They contain informaiton about what the user has granted the application access to, for how long the session is valid and how the token has been encrypted. In most cases, they do not contain any information about the user itself..

Access tokens come in two flavours, standard JWT or opaque. A standard JWT access token looks something like this:

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

These can be decoded using the debugger at [JWT.io](https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c), which allows you to see what data they contain. 

An opaque access token is, well, just that, opaque. They are issued in a way that makes sense only to the issuer, and cannot be decoded in the same way as a JWT access token. The token will generally only be opaque if it is intended for the authorization server. This is the case if you don't supply an audience in the login flow. Generally, the client will want to specify an audience in the login flow because it wants to have access to an API with some user data, for example the user's coupons. This audience would then be the identifier for the coupon API which is configured by the OAuth2 admins of the APIs available.

Access tokens have a finite life time and will expire based on the settings specified for the requesting client.

### Refresh tokens
We use refresh tokens to get new access tokens without having the user re-authenticate. Refresh tokens allows the authorzation server to issue new access tokens when requested.

Refresh tokens have a finite life time and will expire based on the settings specified for the requesting client. They can also be configured for one-time use only, meaning that every time a refresh token is used to issue a new access token a new refresh token is supplied as well.
### ID tokens
ID tokens contains information about the user, but should not be used for authorization. I.e it should not leave the client that obtained the ID token, but the client can inspect it to learn more about the user.

## Elevator-pitch on authorization code

When a user visits a web site or an mobile application and goes to log in, the user is sent to the authorization server to enter their username and password or other means of authentication, such as BankID. 

Once the user has authenticated, the user is sent back to the originating application along with a token that specifies that the user is authenticated. The originating application does not know anything about the authencation process itself, but trust that the authorization server knows what it is doing.


