# Jia Groups Website
[![Libraries Used](https://skillicons.dev/icons?i=js,html,css,py,nginx,django,docker,postgres)](https://skillicons.dev)

## Description

This is the repository for the site hosting on jia.kg domain

## Table of Contents

- [Jia Groups Website](#jia-groups-website)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Required prerequisites](#required-prerequisites)
    - [Installation process](#installation-process)
  - [Usage](#usage)
    - [Local Machine](#local-machine)
    - [Hosting](#hosting)
    - [Admin pannel](#admin-pannel)
    - [Backuping](#backuping)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
  - [Acknowledgments](#acknowledgments)

## Installation

### Required prerequisites

- Docker Engine
- Docker Compose
- Make installed (optional)
- Python 3.8 (optional)
- Domain name and VM (for hosting only)

### Installation process
    
```bash
git clone https://github.com/kermitlafrog61/jia.git
cd jia
cp .env-example .env
```
Fill out all the necessary fields in .env

## Usage

### Local Machine

```bash
make run_dev
```
Wait untill all containers would start, then open localhost

### Hosting

```bash
chmod +x init-letsencrypt.sh
./init-letsencrypt.sh
make run
```
Wait untill all containers would start, then open jia.kg

### Admin pannel

Open /admin/ URL and fill out, what you wrote in .env

### Backuping

1. Create backup dir
```bash
mkdir backup
```
2. Run backups
```bash
chmod +x backup.sh
sudo ./backup.sh
```

## Contributing

Fill free to contribute

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Islam Alybaev – [Linkedin](https://www.linkedin.com/in/kermit-la-frog61/) - islam.alybaev61@gmail.com

## Acknowledgments

This is the code for the website hosting on jia.kg
