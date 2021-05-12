# Troubleshooting

## My access token doesn't look as expected
If you need to read and parse the content of the access token, you need it as a JWT instead of as an opaque access token. To achieve this, you need to specify an `audience` in your login request to Auth0. 

An opaque access token can look something like `Ef4fKOjUa8tsrBQiRuc8bWoG0k2PVNok`, which will not parse as a JWT. If you are unsure about whether or not your access token is a valid JWT, we recommend checking it using the debugger at [JWT.io](https://jwt.io). 

For more information on this, have a look at the [token deep dive](token-deepdive)-page.

## unauthorized_client: Callback URL mismatch. 
You will get this error message if there is a mismatch between the configured callback urls defined in Auth0 and the return url you have specified when calling the authorization endpoint. 

If this happens, please contact the idp-team and have them verify your client config for the specified environments. Common cases are forgetting to specify `https`, missing subdomain (`wwww`), or forgetting case-sensitivity. 