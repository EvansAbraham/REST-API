## Django REST Framework Blog API

This project is a Django REST Framework application for building a blog API. Users can register, create, read, update, and delete blog posts. The application also includes JWT authentication, pagination, search functionality, and the ability to retrieve random blog posts.

### Features

* User registration and JWT authentication (handled by the `account` app)
* CRUD operations for blog posts (potentially handled by the `home` app, functionality depends on app implementation)
* Pagination for displaying blog posts (functionality likely resides in the app handling blog posts)
* Search functionality for finding blog posts by keyword (functionality likely resides in the app handling blog posts)
* Retrieval of random blog posts (functionality likely resides in the app handling blog posts)

### Prerequisites

* Python (version 3.x recommended)
* pip (package installer for Python)
* A code editor or IDE

### Installation

1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

The API will be accessible at http://127.0.0.1:8000/ by default.


### Usage

* Refer to the Django REST Framework documentation for detailed information on using the API: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
* User registration and authentication likely happens under the `/account/` URL path (specific endpoints depend on the `account` app implementation).
* JWT authentication is required for accessing most API endpoints related to blog posts. You can obtain a JWT token by registering a user. Include the JWT token in the Authorization header of subsequent requests.

**Additional Notes**

* Refer to the codebase for specific details on how each endpoint is implemented, including which app handles blog post functionality.
* This is a basic implementation and can be extended further based on your specific needs.


### Contributing

Feel free to fork this repository and contribute by creating pull requests.

**Updates based on URLs:**

* The text mentions that specific functionalities like CRUD for blog posts, search, and random retrieval likely reside in the app mapped to the `/home/` URL path in `urls.py`. This is because the provided URL structure suggests the `account` app might handle user-related functionalities (registration, authentication) while another app might manage blog posts. 
* The example assumes blog post functionality resides under `/api/home/blogs/`. Update the example URL accordingly based on the actual implementation in your code. 
