from setuptools import setup, find_packages

setup(
    name="bard-http-srv",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        # 在这里列出你的库所需的其他Python包
        'bardapi==0.1.23a0',
        'Flask==2.3.2',
    ],

    author="vow1231a",
    author_email="voidmanwzp@gmail.com",
    description="bard http server",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/NullpointerW/bard-http-srv",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)