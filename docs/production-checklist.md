# Pre-production checklist

Before deploying your application to production, you should make sure that you review the following with the IdP-team at Coop

* Session lifetime and time to live for the different tokens
* The use of rotating refresh tokens 
* Make sure you are using the correct tokens
* Double check that your logout urls and callback urls are reachable in production, and that the configured urls have the correct prefixes (https) and subdomain (www)