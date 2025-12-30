# 🎲 TTRPG Hub

A Django-based web application for tabletop RPG enthusiasts to share blog posts, participate in polls, and engage with the TTRPG community.

## ✨ Features

- **Blog System**: Create, read, update, and delete blog posts about TTRPGs
- **Comments**: Engage with posts through a moderated comment system
- **Polls**: Create and vote on TTRPG-related polls with visual pie charts
- **Tags**: Organize and filter content by tags
- **User Authentication**: Modern, secure user registration and login forms
- **Rich Text Editor**: Summernote integration for beautiful post formatting
- **Media Management**: Cloudinary integration for image hosting (production) with local fallback
- **Responsive Design**: Mobile-friendly interface with Bootstrap 5
- **Dynamic Interactions**: AJAX-powered like system with animations
- **Toast Notifications**: Non-intrusive floating notifications

## 🚀 Quick Start (Dev Container)

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com/) or [Cursor](https://cursor.sh/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd TTRPG-Hub
   ```

2. **Open in Dev Container:**
   - Open the project in VS Code/Cursor
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Select "Dev Containers: Reopen in Container"
   - Wait for the container to build (first time takes a few minutes)

3. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
   
   Or use the convenience script:
   ```bash
   bash dev-start.sh
   ```

5. **Access the application:**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## 🛠️ Manual Setup (Without Docker)

If you prefer to run without Docker:

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Copy `.env.example` to `env.py`
   - Update the values with your configuration

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## 📦 Technology Stack

- **Backend**: Django 4.2.4
- **Database**: PostgreSQL (production) / SQLite (development)
- **Authentication**: Django Allauth
- **Rich Text Editor**: Django Summernote
- **Media Storage**: Cloudinary
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Tags**: Django Taggit
- **Deployment**: Render/Heroku ready

## 🗂️ Project Structure

```
TTRPG-Hub/
├── .devcontainer/          # Dev container configuration
│   ├── devcontainer.json   # VS Code/Cursor dev container settings
│   ├── docker-compose.yml  # Docker services (app + database)
│   └── Dockerfile          # Python environment setup
├── blog/                   # Blog app
│   ├── models.py          # Post, Comment models
│   ├── views.py           # Blog views
│   ├── urls.py            # Blog URL patterns
│   └── forms.py           # Blog forms
├── poll/                   # Poll app
│   ├── models.py          # Poll, Vote models
│   ├── views.py           # Poll views
│   └── urls.py            # Poll URL patterns
├── ttrpghub/              # Main project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI configuration
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── media/                 # User-uploaded media
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## 🔧 Configuration

### Environment Variables

The application uses environment variables for configuration. In development (Docker), these are set automatically. For production or manual setup, configure:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `True` for development, `False` for production
- `DATABASE_URL`: PostgreSQL connection string
- `CLOUDINARY_URL`: Cloudinary API credentials
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `CSRF_TRUSTED_ORIGINS`: Comma-separated list of trusted origins

### Database

- **Development**: Uses PostgreSQL in Docker container
- **Production**: Configure via `DATABASE_URL` environment variable
- **Fallback**: SQLite for quick local testing

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📝 Management Commands

### Seed Blog Data
```bash
python manage.py seed_blog
```

### Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🚢 Deployment

The project is configured for deployment on Render or Heroku:

1. Set environment variables in your hosting platform
2. Ensure `DEBUG=False` in production
3. Configure a production PostgreSQL database
4. Set up Cloudinary for media storage
5. Run migrations: `python manage.py migrate`
6. Collect static files: `python manage.py collectstatic`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 📋 Release Notes

### Version 2.0 - December 2025

#### 🎨 UI/UX Improvements
- **Modernized Authentication Forms**: Complete redesign of login, signup, and logout pages with:
  - Professional card-based layouts with gradient backgrounds
  - Password strength indicator with real-time feedback
  - Password visibility toggle for better UX
  - Icon-enhanced input fields
  - "Remember me" functionality
  - Responsive design for all screen sizes
  - Loading states on form submission

- **Enhanced Blog Interactions**:
  - Dynamic like/unlike functionality using AJAX (no page refresh required)
  - Smooth heart animation when liking posts
  - Real-time like count updates
  - Visual feedback with bounce animation

- **Improved Notifications**:
  - Floating toast messages that don't disrupt page layout
  - Centered positioning for better visibility
  - Auto-dismiss after 5 seconds
  - Smooth slide-in animations

#### 🛠️ Local Development Enhancements
- Added local development seed command (`seed_blog_local`) for easy data population
- Improved static and media file serving in development mode
- SQLite fallback for quick local testing without PostgreSQL
- Created default admin user (username: `admin`, password: `admin123`)
- Better environment variable handling for dev/prod separation

#### 🖼️ Image Handling
- Fixed image display in local development environment
- Added placeholder image support for posts without featured images
- Improved image rendering logic in templates
- Copied hero background image to static folder for reliability

#### 🐛 Bug Fixes
- Fixed HTML tags appearing in blog post excerpts (added `striptags` filter)
- Fixed like button not updating without page refresh
- Fixed checkbox styling on authentication forms
- Corrected URL routing order to prevent pattern conflicts
- Added authentication checks to prevent errors on like/unlike actions

#### 📱 Responsive Design
- All new UI components are mobile-first and fully responsive
- Touch-friendly button sizes and spacing
- Proper viewport handling on tablets and phones

#### 🔧 Technical Improvements
- Added `auth-forms.js` for enhanced authentication form interactions
- Enhanced `likes.js` with proper CSRF handling and error management
- Expanded `style.css` with modern CSS techniques (gradients, animations, flexbox)
- Improved view layer to support AJAX responses
- Better separation of concerns in templates

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Code Institute for the project template
- Django community for excellent documentation
- Bootstrap for the UI framework
- Font Awesome for icons
- All contributors and users of TTRPG Hub

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

Made with ❤️ for the TTRPG community
