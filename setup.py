import setuptools

with open('README.md', 'r', encoding='u8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='lencode',
    version='0.1.2',
    author='linupy',
    author_email='linupy@163.com',
    description='编码/加密工具包 Encoding/Encryption Toolkit',
    url='https://github.com/linupychiang/lencode',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    install_requires=[],
    python_requires='>=3',
)
