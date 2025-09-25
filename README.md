# SRA_project


SRA_Project/
│
├── main/                         
│   ├── templates/main/
│   │   ├── base.html          # global base template
│   │   ├── index.html         # public homepage (before login)
│   │   └── includes/
│   │       ├── navbar.html
│   │       ├── footer.html
│   │       └── hero.html
│
├── dashboard/                    
│   ├── templates/dashboard/
│   │   └── dashboard.html     # charts, graphs (after login landing page)
│
├── users/                        
│   ├── templates/users/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   └── password_reset.html
│
├── static/                       
│   ├── css/
│   ├── js/
│   └── images/
│
└── manage.py
