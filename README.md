<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RomainLefeuvre/SonarQubeToolkit">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">SonarQubeToolkit</h3>
Tool for extracting measures from each sonarqube project.
  <p align="center">
    project_description
    <br />
    <br />
    <a href="https://github.com/RomainLefeuvre/SonarQubeToolkit/issues">Report Bug</a>
    ·
    <a href="https://github.com/RomainLefeuvre/SonarQubeToolkit/issues">Request Feature</a>
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



### Built With

* [Python](https://www.python.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3.10
* Docker
* Docker-Compose 

### Installation

1. Generate a token from your Sonarqube instance or deploy a new one
   To deploy an instance please run 
   ```
   cd SonarQube
   docker-compose up 
   ```
2. Clone the repo
   ```sh
   git clone https://github.com/RomainLefeuvre/SonarQubeToolkit.git
   ```
3. Install dependencies
   The requirements.txt file list all Python libraries that you need to run the project
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API in `config.ini`
   ```js
   [sonarQube]
   host = localhost
   port = 9000
   token = your_token
   ```
5. Use sonarqube_toolkit in your code (exemple in MeasuresToSpyderGraph.ipynb)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage



<!-- ROADMAP -->
## Roadmap

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

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/RomainLefeuvre/SonarQubeToolkit](https://github.com/RomainLefeuvre/SonarQubeToolkit)

<p align="right">(<a href="#top">back to top</a>)</p>




<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/RomainLefeuvre/SonarQubeToolkit.svg?style=for-the-badge
[contributors-url]: https://github.com/RomainLefeuvre/SonarQubeToolkit/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/RomainLefeuvre/SonarQubeToolkit.svg?style=for-the-badge
[forks-url]: https://github.com/RomainLefeuvre/SonarQubeToolkit/network/members
[stars-shield]: https://img.shields.io/github/stars/RomainLefeuvre/SonarQubeToolkit.svg?style=for-the-badge
[stars-url]: https://github.com/RomainLefeuvre/SonarQubeToolkit/stargazers
[issues-shield]: https://img.shields.io/github/issues/RomainLefeuvre/SonarQubeToolkit.svg?style=for-the-badge
[issues-url]: https://github.com/RomainLefeuvre/SonarQubeToolkit/issues
[license-shield]: https://img.shields.io/github/license/RomainLefeuvre/SonarQubeToolkit.svg?style=for-the-badge
[license-url]: https://github.com/RomainLefeuvre/SonarQubeToolkit/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
