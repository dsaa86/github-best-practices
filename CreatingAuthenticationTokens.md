# Creating Authentication Tokens

Authentication tokens are the method by which you can verify that you are authorised to use the Github account that is attempting to make changes to a repo on Github.

These tokens replace the traditional username and password combination, instead you use a username with a token.

Tokens are generated using a hashing algorithm, which makes them inherently more secure than passwords for authentication between client and server. Tokens have a maximum validity period to ensure that a user session does not continue indefinitely.

Best practice is to keep the validity of a token as short as is practicable. In reality, a validity of 20-30 days offers a reasonable balance between security and time between re-authentication.

You can read Github's documentation on generating an authorisation token [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
