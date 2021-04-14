# Troubleshooting

## My access token doesn't look as expected
If you need to read and parse the content of the access token, you need it as a JWT instead of as an opaque access token. To achieve this, you need to specify an `audience` in your login request to Auth0. 

An opaque access token can look something like `Ef4fKOjUa8tsrBQiRuc8bWoG0k2PVNok`, which will not parse as a JWT. If you are unsure about whether or not your access token is a valid JWT, we recommend checking it using the debugger at [JWT.io](https://jwt.io). 

For more information on this, have a look at the [token deep dive](token-deepdive)-page.