<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!-- 
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Racerin/pdf_encrypt_dir">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Encrypt PDF Directory</h3>

  <p align="center">
    Encrypt all PDF files and recursive directories' PDF files.
    <br />
    <a href="https://github.com/Racerin/pdf_encrypt_dir/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Racerin/pdf_encrypt_dir">View Demo</a>
    ·
    <a href="https://github.com/Racerin/pdf_encrypt_dir/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/Racerin/pdf_encrypt_dir/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://www.thewindowsclub.com/wp-content/uploads/2019/03/Password-protect-PDF-documents-with-LibreOffice.png)

The aim of this project is to simplify encrypting PDF documents. No 3rd party software required. Just run the program, enter the appropriate inputs and VOILA, your documents are encrypted. So far, it's done in the command line.
<!-- <br>
Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `linked_in`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description` -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

<!-- * [![Next][Next.js]][Next-url] -->
<!-- * [![React][React.js]][React-url] -->
<!-- * [![Vue][Vue.js]][Vue-url] -->
<!-- * [![Angular][Angular.io]][Angular-url] -->
<!-- * [![Svelte][Svelte.dev]][Svelte-url] -->
<!-- * [![Laravel][Laravel.com]][Laravel-url] -->
<!-- * [![Bootstrap][Bootstrap.com]][Bootstrap-url] -->
<!-- * [![JQuery][JQuery.com]][JQuery-url] -->
* [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Thus far, this program must be installed using python (a standalone version would be created soon). First, ensure you have Python version 3 on your computer. 
<br>Then, download the files from the repository.
<!-- This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps. -->

### Prerequisites

For now, this program requires Python version 3.10 or older to run. Visit the [Python](https://www.python.org/downloads/) website for more details.
<!-- * npm
  ```sh
  npm install npm@latest -g
  ``` -->

### Installation

<!-- 1. Get a free API Key at [https://example.com](https://example.com) -->
1. Clone the repository
   ```sh
   git clone https://github.com/Racerin/pdf_encrypt_dir.git
   ```
2. Set up your virtual environment
   #### Windows (Powershell/cmd):
   ```ps
   python -m venv venv
   ... (Success message)
   venv/Scripts/activate
   ```
   #### Linux (Bash):
   ```sh
   python -m venv venv
   ... (Success message)
   source venv/Scripts/activate
   ```
3. Install 3rd party packages
   ```
   pip install -r requirements.txt
   ```
<!-- 3. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ``` -->
   And you are finished. Now you could run the program.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<!-- Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->

This program works via the command line interface (CLI). 
Use the following command it initiate the program.
```
python -m main
```
<br>Use the 'help' command to see the funtionalities available and the arguments.
```
python -m main --help
```
Here is a snippet of what you could do with the program.
```
Options:
  --user_password TEXT   Password for encrypting PDF documents.
  --owner_password TEXT  Password for encrypting PDF documents. Grants full
                         access.
  --read_dir TEXT        Directory of PDF files to encrypt.
  --write_dir TEXT       Directory of files to place encrypted PDF files..
  --help                 Show this message and exit.
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

<!-- - [ ] Feature 2 -->
<!-- - [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature -->

See the [open issues](https://github.com/Racerin/pdf_encrypt_dir/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Darnell Baird - [@linked_in](https://tt.linkedin.com/in/darnell-baird-3d) - drsbaird@yahoo.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* No one else at this point
<!-- * [Darnell Baird (Racerin)](https://github.com/Racerin) -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Racerin/pdf_encrypt_dir.svg?style=for-the-badge
[contributors-url]: https://github.com/Racerin/pdf_encrypt_dir/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Racerin/pdf_encrypt_dir.svg?style=for-the-badge
[forks-url]: https://github.com/Racerin/pdf_encrypt_dir/network/members
[stars-shield]: https://img.shields.io/github/stars/Racerin/pdf_encrypt_dir.svg?style=for-the-badge
[stars-url]: https://github.com/Racerin/pdf_encrypt_dir/stargazers
[issues-shield]: https://img.shields.io/github/issues/Racerin/pdf_encrypt_dir.svg?style=for-the-badge
[issues-url]: https://github.com/Racerin/pdf_encrypt_dir/issues
[license-shield]: https://img.shields.io/github/license/Racerin/pdf_encrypt_dir.svg?style=for-the-badge
[license-url]: https://github.com/Racerin/pdf_encrypt_dir/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
<!-- My entry -->
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://Python.org 