# obfus_socat

 is a project that encapsulates connections using  through SSL or SSH, aiming to provide secure communication tunnels.

## Installation

To install the required dependencies, run:

```sh
docker build -t obfus_socat .
```

## Configuration

- Ensure you have SSL certificates in the  folder:  and .
- Adjust your  as necessary for different environments.

## Usage

Example usage of  script:

```sh
python obfus_socat.py --mode ssl --local_port 1080 --remote_host example.com --remote_port 443
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.
