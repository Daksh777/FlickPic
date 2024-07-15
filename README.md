# FlickPic

FlickPic is an open-source Flickr picture sharing website built with Django and HTMX. It allows users to easily share and interact with Flickr content in a user-friendly interface.

## Features

- **Automatic Flickr Post Import**: Users can enter a Flickr URL, and our webcrawler will automatically fetch all the details for the post.
- **User Interactions**: 
  - Comment on posts
  - Like posts
  - Create and assign categories/tags
- **Content Discovery**:
  - View top posts
  - See top comments
- **Real-time Updates**: Powered by HTMX for a smooth, app-like experience without full page reloads

## Tech Stack

- Backend: Django
- Frontend Enhancement: HTMX, Tailwind CSS
- Database: SQLite
- Web Scraping: BeautifulSoup

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Daksh777/flickpic.git
   cd flickpic
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

1. Navigate to `http://localhost:8000` in your web browser.
2. Sign up for an account or log in.
3. To share a Flickr post, simply paste the Flickr URL into the provided input field.
4. Explore posts, like, comment, and add tags as desired.

## Database

FlickPic uses Django's default database setup, which is SQLite. This makes the project easy to set up and run locally without any additional database configuration. 

If you need to switch to a different database in the future (e.g., for production deployment), you can modify the `DATABASES` configuration in `settings.py`. Django's ORM makes it relatively straightforward to switch between different database backends.
