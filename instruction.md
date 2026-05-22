Fix the intermittent authentication failures

We have been seeing frequent intermittent authentication failures in production after some recent infrastructure migration.

Users can log in successfully, but refreshing the page or retrying authenticated requests causes valid sessions to get rejected unexpectedly.

Investigate the authentication flow keenly and fix the issue without changing the external API behavior.