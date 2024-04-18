## FLICK FUSION

This is an app designed to allow customers to buy movies as well as book seats in cinemas.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation

Provide instructions on how to install and set up your backend project. Include any prerequisites, dependencies, or database setup required.


## USAGE

1. Start the server
2. Open your preferred API testing tool
3. Send requests to the API endpoints listed in the API documentation.


## API DOCUMENTATION

-JWT authentication
  -We used jwt authentication to authenticate users
  -The was a protected route where logged in in users will be redirected to while the unprotected route was used for the users who did not have one.

-Routes
 -/movies route
    -This route was used to redirect users to the movies page where they will be able to but movies
 -/Ontheatre route
    -This route was used to redirect users to to the page where it shows if movies are being show in the cinema as well as where they can book.

- GET /api/users
  - Description: Get a list of all users.
  - Request: None
  - Response: Array of user objects
  
- POST /api/users
  - Description: Create a new user.
  - Request: JSON object with user data
  - Response: Created user object
  

## CONTRIBUTING

- Report bugs or suggest features by opening an issue.
- Fork the repository and create a new branch for your contribution.
- Submit a pull request with your changes.

## LICENSE


Feel free to customize this template to better fit the specifics of your backend project. You can add or remove sections, provide more detailed instructions, or include additional information as needed.

