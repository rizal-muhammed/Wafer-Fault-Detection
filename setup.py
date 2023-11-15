import setuptools

# read 'README.md' file
with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

# defining version
__version__ = "0.0.0"

REPO_NAME = "Wafer-Fault-Detection"
AUTHOR_USER_NAME = "rizal-muhammed"
SRC_REPO = "wafer_fault_detection"
AUTHER_EMAIL = "rizalmuhammedm.p@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    description="A Classification Machine Learning Project for Wafer Fault Detection.",
    long_description=long_description,
    author=AUTHOR_USER_NAME,
    author_email=AUTHER_EMAIL,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    keywords=['machine learning', 'data science'],
    license='MIT',
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    }
)