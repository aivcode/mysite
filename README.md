# Django Tutorial
[Link to Django Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)

[Link to Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

## Git initial setup
### Your Identity
The first thing you should do when you install Git is to set your user name and email address. This is important because every Git commit uses this information, and it’s immutably baked into the commits you start creating:
```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```
Again, you need to do this only once if you pass the --global option, because then Git will always use that information for anything you do on that system. If you want to override this with a different name or email address for specific projects, you can run the command without the --global option when you’re in that project.

## Hiding SECRET_KEY
```pip install python-dotenv```

Create **.env** in project root

```SECRET_KEY=key_from_settings.py```

Then, in **settings.py**:
```python
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = str(os.getenv('SECRET_KEY'))
```

## Models
### Three-step guide to making model changes:
- Change your models (in models.py)
- Run ```python manage.py makemigrations``` to create migrations for those changes
- Run ```python manage.py migrate``` to apply those changes to the database.

The reason that there are separate commands to make and apply migrations is because you’ll commit migrations to your version control system and ship them with your app; they not only make your development easier, they’re also usable by other developers and in production.
