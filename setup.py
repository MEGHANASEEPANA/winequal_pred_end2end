import setuptools

# Read the README file for long description (optional, if you have README.md)
# Uncomment the next block if you have a README.md
# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()

# Or provide a simple description if you don’t want to load README:
long_description = "A comprehensive ML project for wine quality prediction."

__version__ = "0.0.0"

REPO_NAME = "winequal_pred_end2end"
AUTHOR_USER_NAME = "SEEPANA MEGHANA"
SRC_REPO = "winequality"
AUTHOR_EMAIL = "meghana2805@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,  # Add this or keep README.md block
    long_description_content_type="text/markdown",  # Correct the typo here
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
