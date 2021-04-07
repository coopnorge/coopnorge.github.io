
This is extra detailed info, and it is expected that you have an understanding of which flow you will use by reading for example [auth0 docs](https://auth0.com/docs/authorization/which-oauth-2-0-flow-should-i-use) and understanding that.

## Getting access tokens
When you do one of the flows, you will have the option to specify scope parameters. This can be confusing so we will try to make it more clear. Scopes are requested by supplying the `scope` parameter in the request. This is an example request. The scopes `(openid,profile,email,phone)` are part of the openid standard, which means that your application will get an ID token back. The openid scope is the only required scope for getting an ID token, and the others simple give more data in the ID token. Next comes the `offline_access`, which means that you want a refresh token. See the section on refresh tokens for this. The `audience` is neccessary to get an access token that can be used against the API identified by that audience. It is quite logical, you can think _who is the audience/the entity that my application wants to talk to?_
This will depend and you will have to refer to the documentation for the coop APIs that we have posted in this repo. You can only ever ask for one audience. The API may also support scopes, which would then be added to the list of scopes in the request. This is a way to limit the access to an api. For example, the API could have registered your application to only have access to reading data but not updating data. All of this behaviour is configured by the admins of the OAuth2 infrastructure of Coop. The APIs are however responsible to enforce this policy, i.e they have to inspect incoming access tokens and see if they have the right scopes for the request you application is doing.
```
Request URL: https://login.developer.coop/authorize?client_id=<your client id>&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&response_type=code&scope=openid+profile+email+phone+offline_access&state=f4joN6Yn5ZxKVTSXaxhkTh8ogqqX3TOzCPyLrXhn2Pc%3D&audience=https://integration.coop.no/legacy
```

#### Multiple audience in access token
There is a little caveat here which is that the accesstoken will contain two audiences if you used the `openid` scope. The point is that the authorization server can answer with userinfo from its `/userinfo` endpoint which will essentially give the contents of the id token.


## Refresh tokens
_Note: Auth0 Management API does not support refresh tokens. For the other APIs it can be enabled/disabled through the Auth0 config in terraform._

To obtain a refresh token, the client starting the login sequence (this will often be the authorization code flow)
must specify at least the scope `offline_access` in the request url.
This will make the authorization server return both an access token and a refresh token *if the API specified by the `&audience` supports it*. This refresh token can then be used by specifying `grant_type=refresh_token` and sending the refresh token like in the example below. Without using refresh tokens, the user would have to log in again (through the authorization code flow) when the access token has expired.

```
curl --request POST \
  --url 'https://coopno-developer.eu.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=refresh_token \
  --data 'client_id=YOUR_CLIENT_ID' \
  --data client_secret=YOUR_CLIENT_SECRET \
  --data refresh_token=YOUR_REFRESH_TOKEN
```

