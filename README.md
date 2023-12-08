Agri Space is a comprehensive platform designed to assist users in various aspects of agriculture. It combines three main functionalities:

1. Weather Forecasting: Provides real-time weather updates based on the user's location. This feature helps users plan their agricultural activities more effectively.

2. Marketplace: A dedicated space for users to post and view classified ads related to agriculture. This feature facilitates the buying and selling of agricultural products and equipment.

3. Plant Disease Recognition: An AI-powered feature that recognizes plant diseases. Users can submit an image of their plant, and the AI will analyze it to identify any potential diseases.

## Installation

1. Clone the Repository:
$ git clone <repository_url>
$ cd <repository_directory>

2. Install Dependencies:
$ pip install -r requirements.txt

3. Download Model, .env, and Static Files: Download the AI model, .env file, and other static files from Google Drive. Place all the downloaded files in the appropriate directories as per your project structure.

4. Run Migrations:
$ python manage.py makemigrations
$ python manage.py migrate

5. Run the Development Server:
$ python manage.py runserver
The development server should be running at http://127.0.0.1:8000/.

## API Endpoints

### Weather Endpoint:
- POST /weather: Get current weather information by providing a location.

### Marketplace Endpoints:
- POST /addPost: Authenticate and create a new classified ad post.
- DELETE /delete/{post_id}: Authenticate and delete a specific classified ad post.
- GET /getUserPosts: Authenticate and get the posts created by the authenticated user.
- GET /getPosts/{category}: Get classified ad posts by category.

### AI Endpoints:
- POST /submit: Authenticate and submit an image for plant disease recognition.

## Important Notes

Ensure that you have the required environment variables in the .env file, including the WEATHER_KEY for accessing the weather API. Make sure the AI model is correctly placed in the project directory. For security reasons, it’s recommended to use environment variables for sensitive information such as secret keys.

## Project Contributors

- Seif Ddine Ben Amara
- Khaled Hammami
- Ghizlen Maarouf
