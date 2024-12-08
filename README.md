# Proxy Viability Testing

This project is designed to test the viability of proxies retrieved from the Webshare API. The script retrieves a list of proxies, tests their viability asynchronously, and logs the results.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/KeaganGilmore/proxy-viability-testing.git
    cd proxy-viability-testing
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    poetry install
    ```

4. Create a `.env` file in the root directory and add your Webshare API key:
    ```dotenv
    API_KEY=your_api_key_here
    ```

## Contact

- **Email:** [keagangilmore@gmail.com](mailto:keagangilmore@gmail.com)
- **Discord:** [keagan2980](https://discord.com/users/keagan2980)

## Usage

Run the script to test the viability of the proxies:
```sh
python main.py